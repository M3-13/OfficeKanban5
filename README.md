# OfficeKanban5

Ein einfaches Kanban-Board mit Multi-User-Authentifizierung. Benutzer registrieren sich, loggen sich per JWT ein und verwalten ihre eigenen Boards mit Karten in den Spalten To Do, In Progress und Done.

## Tech-Stack

- **Backend**: Python 3.12+, FastAPI, SQLAlchemy, SQLite
- **Auth**: python-jose (JWT), bcrypt (Passlib)
- **Frontend**: React 19, TypeScript, Vite
- **HTTP-Client (Frontend)**: Axios

## Projektstruktur

```
backend/         FastAPI-Backend (Python)
  main.py        App-Einstiegspunkt, CORS, Router, Health-Check
  config.py      Umgebungskonfiguration (JWT, DB)
  database.py    SQLAlchemy-Engine, Session, Base
  models.py      User, Board, Card
  auth.py        JWT-Auth (Token, Hash, Current-User-Dependency)
  schemas.py     Pydantic-Modelle für Request/Response
  routers/       API-Endpunkte (auth, boards)
  tests/         Pytest-Tests

frontend/        Vite + React + TypeScript
  src/           Anwendungscode (Komponenten, Seiten, API, Context)
```

## Setup

### Voraussetzungen

- Python 3.12+
- Node.js 20+

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Unix
pip install -r requirements.txt
```

### Frontend

```bash
cd frontend
npm install
```

## Start

### Backend

```bash
cd backend
set JWT_SECRET=dein-sicheres-secret
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm run dev
```

## Umgebungsvariablen

| Variable | Beschreibung | Default |
|---|---|---|
| `JWT_SECRET` | Geheimer Schlüssel für JWT-Signierung | **kein Default - muss gesetzt sein** |
| `FRONTEND_ORIGIN` | Erlaubte CORS-Origin | `http://localhost:5173` |

## API-Endpunkte

### Health

| Methode | Pfad | Beschreibung |
|---|---|---|
| `GET` | `/health` | Gibt `{"status": "ok"}` zurück |

### Auth (STUB)

| Methode | Pfad | Beschreibung |
|---|---|---|
| `POST` | `/auth/register` | Benutzer registrieren |
| `POST` | `/auth/login` | Login (gibt JWT-Token zurück) |

### Boards & Karten (STUB)

| Methode | Pfad | Beschreibung |
|---|---|---|
| `GET` | `/api/boards` | Alle Boards des Benutzers |
| `POST` | `/api/boards` | Board erstellen |
| `GET` | `/api/boards/{id}/cards` | Karten eines Boards |
| `POST` | `/api/boards/{id}/cards` | Karte erstellen |
| `PUT` | `/api/cards/{id}` | Karte aktualisieren |
| `DELETE` | `/api/cards/{id}` | Karte löschen |
| `PATCH` | `/api/cards/{id}/status` | Karten-Status ändern |

## Features

- Multi-User-Authentifizierung mit JWT
- Board- und Kartenverwaltung (Kanban)
- Drag & Drop zwischen den Spalten
- SQLite-Datenbank (keine externe DB nötig)

## Tests

```bash
cd backend
py -m pytest
```

## Frontend Build

```bash
cd frontend
npm run build
```
