# MEDIBUDDY - Smart Medication and Wellness Platform

**Your Health. Your Schedule. Your Care.**

MEDIBUDDY is a medication organisation and personal wellness dashboard developed by Nilutpal Konch.

## About

MEDIBUDDY helps users organise their medication schedules, record medication activity and maintain personal wellness records through a simple web application.

## Features

- Medication management: add, edit and delete medicines
- Today's medication schedule
- Medication activity tracking
- Medicine stock overview
- Low-stock overview
- Wellness activity timer
- Daily activity goals
- Seven-day activity chart
- Personal reflection notes
- Local activity history
- English, Assamese and Hindi interface labels
- Responsive dashboard
- Assamese-inspired interface design
- No camera functionality

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application and API |
| SQLite | Local database |
| HTML | Frontend structure |
| CSS | Interface design |
| JavaScript | Frontend functionality |
| Git and GitHub | Version control |
| Render | Cloud deployment |

## Project Structure

`	ext
MEDIBUDDY/
|-- backend/
|   |-- app.py
|   |-- requirements.txt
|-- frontend/
|   |-- index.html
|   |-- style.css
|   |-- app.js
|-- data/
|-- .gitignore
|-- README.md
|-- SETUP_WINDOWS.txt
`

## Installation on Windows

1. Clone the repository:

`powershell
git clone https://github.com/nilutpalkonch88-pixel/medibuddy-backend.git
`

2. Open the project directory:

`powershell
cd medibuddy-backend
`

3. Create a virtual environment:

`powershell
py -3.10 -m venv venv
`

4. Activate it:

`powershell
.\venv\Scripts\Activate.ps1
`

5. Install dependencies:

`powershell
pip install -r backend/requirements.txt
`

6. Start the application:

`powershell
cd backend
python app.py
`

Open the local address printed by Flask in your browser.

## Medical Disclaimer

MEDIBUDDY is a personal organisation and wellness-tracking prototype. It does not diagnose conditions, prescribe medicines or replace qualified healthcare professionals. Always follow the instructions provided by your healthcare professional.

## Developer

**Nilutpal Konch**

Project: MEDIBUDDY  
Domain: Healthcare Technology  
Development: Hackathon Project  
Year: 2026

---

**Developed by Nilutpal Konch © 2026**
