from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from pathlib import Path
import sqlite3
from datetime import date, datetime

ROOT = Path(__file__).resolve().parent.parent
FRONTEND = ROOT / "frontend"
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "medibuddy.db"

app = Flask(__name__, static_folder=str(FRONTEND), static_url_path="")
CORS(app)

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    with db() as con:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dosage TEXT NOT NULL DEFAULT '',
            medicine_time TEXT NOT NULL DEFAULT '',
            stock INTEGER NOT NULL DEFAULT 0,
            instructions TEXT NOT NULL DEFAULT '',
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS medication_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            medicine_id INTEGER NOT NULL,
            medicine_name TEXT NOT NULL,
            status TEXT NOT NULL,
            log_date TEXT NOT NULL,
            logged_at TEXT NOT NULL,
            FOREIGN KEY(medicine_id) REFERENCES medicines(id) ON DELETE CASCADE
        );
        """)

@app.get("/")
def home():
    return send_from_directory(FRONTEND, "index.html")

@app.get("/api/health")
def health():
    return jsonify({"ok": True, "app": "MEDIBUDDY 3.0"})

@app.get("/api/medicines")
def get_medicines():
    with db() as con:
        rows = con.execute("SELECT * FROM medicines ORDER BY id DESC").fetchall()
    return jsonify([dict(r) for r in rows])

@app.post("/api/medicines")
def add_medicine():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    if not name:
        return jsonify({"error": "Medicine name is required."}), 400
    dosage = str(data.get("dosage", "")).strip()
    medicine_time = str(data.get("medicine_time", "")).strip()
    instructions = str(data.get("instructions", "")).strip()
    try:
        stock = max(0, int(data.get("stock", 0)))
    except (TypeError, ValueError):
        return jsonify({"error": "Stock must be a whole number."}), 400
    with db() as con:
        cur = con.execute(
            """INSERT INTO medicines(name,dosage,medicine_time,stock,instructions,created_at)
               VALUES(?,?,?,?,?,?)""",
            (name, dosage, medicine_time, stock, instructions, datetime.now().isoformat(timespec="seconds"))
        )
        row = con.execute("SELECT * FROM medicines WHERE id=?", (cur.lastrowid,)).fetchone()
    return jsonify(dict(row)), 201

@app.put("/api/medicines/<int:medicine_id>")
def update_medicine(medicine_id):
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    if not name:
        return jsonify({"error": "Medicine name is required."}), 400
    try:
        stock = max(0, int(data.get("stock", 0)))
    except (TypeError, ValueError):
        return jsonify({"error": "Stock must be a whole number."}), 400
    with db() as con:
        cur = con.execute(
            """UPDATE medicines SET name=?, dosage=?, medicine_time=?, stock=?, instructions=?
               WHERE id=?""",
            (name, str(data.get("dosage", "")).strip(),
             str(data.get("medicine_time", "")).strip(), stock,
             str(data.get("instructions", "")).strip(), medicine_id)
        )
        if cur.rowcount == 0:
            return jsonify({"error": "Medicine not found."}), 404
        row = con.execute("SELECT * FROM medicines WHERE id=?", (medicine_id,)).fetchone()
    return jsonify(dict(row))

@app.delete("/api/medicines/<int:medicine_id>")
def delete_medicine(medicine_id):
    with db() as con:
        cur = con.execute("DELETE FROM medicines WHERE id=?", (medicine_id,))
        if cur.rowcount == 0:
            return jsonify({"error": "Medicine not found."}), 404
    return jsonify({"ok": True})

@app.get("/api/schedules/today")
def today_schedule():
    today = date.today().isoformat()
    with db() as con:
        medicines = con.execute("SELECT * FROM medicines ORDER BY medicine_time, name").fetchall()
        logs = con.execute(
            "SELECT medicine_id,status FROM medication_logs WHERE log_date=?", (today,)
        ).fetchall()
    status = {r["medicine_id"]: r["status"] for r in logs}
    result = []
    for m in medicines:
        item = dict(m)
        item["status"] = status.get(m["id"], "pending")
        result.append(item)
    return jsonify(result)

@app.post("/api/logs")
def add_log():
    data = request.get_json(silent=True) or {}
    try:
        medicine_id = int(data.get("medicine_id"))
    except (TypeError, ValueError):
        return jsonify({"error": "Valid medicine_id is required."}), 400
    status = str(data.get("status", "taken")).lower()
    if status not in ("taken", "skipped"):
        return jsonify({"error": "Status must be taken or skipped."}), 400
    today = date.today().isoformat()
    with db() as con:
        med = con.execute("SELECT * FROM medicines WHERE id=?", (medicine_id,)).fetchone()
        if not med:
            return jsonify({"error": "Medicine not found."}), 404
        existing = con.execute(
            "SELECT id FROM medication_logs WHERE medicine_id=? AND log_date=?",
            (medicine_id, today)
        ).fetchone()
        if existing:
            con.execute(
                "UPDATE medication_logs SET status=?, logged_at=? WHERE id=?",
                (status, datetime.now().isoformat(timespec="seconds"), existing["id"])
            )
        else:
            con.execute(
                """INSERT INTO medication_logs(medicine_id,medicine_name,status,log_date,logged_at)
                   VALUES(?,?,?,?,?)""",
                (medicine_id, med["name"], status, today, datetime.now().isoformat(timespec="seconds"))
            )
        if status == "taken":
            con.execute(
                "UPDATE medicines SET stock=MAX(0,stock-1) WHERE id=? AND stock>0",
                (medicine_id,)
            )
    return jsonify({"ok": True, "status": status})

@app.get("/api/logs")
def get_logs():
    with db() as con:
        rows = con.execute("SELECT * FROM medication_logs ORDER BY id DESC LIMIT 100").fetchall()
    return jsonify([dict(r) for r in rows])

@app.get("/api/stats")
def stats():
    today = date.today().isoformat()
    with db() as con:
        total = con.execute("SELECT COUNT(*) n FROM medicines").fetchone()["n"]
        low = con.execute("SELECT COUNT(*) n FROM medicines WHERE stock<=5").fetchone()["n"]
        taken = con.execute(
            "SELECT COUNT(*) n FROM medication_logs WHERE log_date=? AND status='taken'", (today,)
        ).fetchone()["n"]
        skipped = con.execute(
            "SELECT COUNT(*) n FROM medication_logs WHERE log_date=? AND status='skipped'", (today,)
        ).fetchone()["n"]
    return jsonify({"total_medicines": total, "low_stock": low, "taken_today": taken, "skipped_today": skipped})

@app.get("/<path:path>")
def frontend_files(path):
    candidate = FRONTEND / path
    if candidate.is_file():
        return send_from_directory(FRONTEND, path)
    return jsonify({"error": "Not found"}), 404

init_db()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
