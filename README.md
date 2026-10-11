# GrantLens

AI-Powered Grant Audit & Evaluation Platform — CSE299 Section 3, Group 2

## Week 1 Milestone

A full-stack web application with a **React + Vite** frontend and a **Django 6.1 + DRF** backend, connected via REST API.

### Tech Stack

| Layer | Technologies |
|-------|-------------|
| Frontend | React 18, Vite, Tailwind CSS v3, Lucide React |
| Backend | Django 6.1, Django REST Framework, django-cors-headers |
| Database | SQLite (Week 1), PostgreSQL (planned Week 2) |

### Running the Project

**Terminal 1 — Backend:**
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

**Terminal 2 — Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Open **http://localhost:5173** in your browser.

### API Endpoint

`GET http://127.0.0.1:8000/api/status/` — Returns live platform metrics as JSON.
