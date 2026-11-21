# medibuddy-backend
A smart healthcare and medication management platform built with Python Flask, helping patients and caregivers organise medication schedules, track adherence and manage daily healthcare routines.
# 💊 MEDIBUDDY — Smart Healthcare & Medication Management Platform

<p align="center">
  <strong>Your Health. Your Schedule. Your Care.</strong>
</p>

<p align="center">
  A smart healthcare platform designed to help individuals, elderly people and caregivers organise medication schedules and manage daily healthcare routines.
</p>

---

## 🚀 About the Project

MEDIBUDDY is a healthcare technology project developed to address one of the common challenges in everyday healthcare: forgetting medication schedules.

The platform aims to provide an accessible and user-friendly digital solution for organising medicines, tracking medication routines and supporting caregivers.

This repository contains the backend foundation of MEDIBUDDY.

## 🎯 Problem Statement

Many individuals, particularly elderly people, struggle to remember their daily medication schedules. Missing scheduled medicines can make healthcare routines difficult to manage.

MEDIBUDDY aims to simplify medication organisation through a centralised digital platform.

## ✨ Planned Features

- Medication schedule management
- Smart medication reminders
- Medication history tracking
- Daily adherence analytics
- Patient and caregiver portal
- Medicine inventory management
- Low-stock and expiry notifications
- Healthcare appointment management
- Accessible interface for elderly users
- Multilingual support
- AI-powered general healthcare assistance

*Features will be implemented progressively.*

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | REST API framework |
| Flask-SQLAlchemy | Database ORM |
| PostgreSQL | Production database |
| SQLite | Local development database |
| Git & GitHub | Version control |
| Render | Backend deployment |

## 📁 Project Structure

```text
backend/
│
├── routes/
├── instance/
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/medibuddy-backend.git
```

### 2. Enter the project directory

```bash
cd medibuddy-backend
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the backend directory.

```env
APP_NAME=MediBuddy
APP_VERSION=1.0.0
FLASK_DEBUG=1
DATABASE_URL=sqlite:///medibuddy.db
CORS_ORIGINS=http://localhost:5500,http://127.0.0.1:5500
```

Use a secure secret key when required by the application configuration. Never commit real credentials or secrets.

### 7. Run the backend

```bash
python app.py
```

## 🔍 API Health Check

Once the backend is running, visit:

```text
http://127.0.0.1:5000/api/health
```

Expected response:

```json
{
  "status": "healthy",
  "application": "MediBuddy",
  "version": "1.0.0"
}
```

## ☁️ Deployment

The backend is designed for deployment using cloud hosting platforms such as Render.

Deployment configuration:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Database: PostgreSQL
- Environment variables: Configure securely through the hosting dashboard.

## 🔐 Security

Security considerations include:

- Environment-based configuration
- Password hashing when authentication is implemented
- Protected API endpoints
- Database access controls
- Secure handling of sensitive information

## 🗺️ Development Roadmap

- [x] Phase 1 — Flask backend foundation
- [x] Phase 1 — Health-check API
- [ ] Phase 2 — User authentication
- [ ] Phase 3 — Medication management API
- [ ] Phase 4 — Reminder system
- [ ] Phase 5 — Patient dashboard
- [ ] Phase 6 — Caregiver portal
- [ ] Phase 7 — Health analytics
- [ ] Phase 8 — Production deployment

## 👨‍💻 Developer

**Nilutpal Konch**

Project: MEDIBUDDY  
Domain: Healthcare Technology  
Project Type: Hackathon Development

## ⚠️ Medical Disclaimer

MEDIBUDDY is a software development prototype intended to support medication organisation and healthcare routines. It does not provide medical diagnosis, prescribe medicines or replace professional medical advice.

Always follow instructions from qualified healthcare professionals.

---

<p align="center">
  <strong>MEDIBUDDY — Making Healthcare Routines Easier.</strong>
</p>

<p align="center">
  Developed with ❤️ by Nilutpal Konch
</p>
