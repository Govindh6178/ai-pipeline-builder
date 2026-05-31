# AI Pipeline Builder

A visual drag-and-drop AI pipeline builder that lets you design and validate AI workflows through an intuitive node-based interface.

## Features

- **Visual Pipeline Builder** — Drag and drop nodes to design AI workflows
- **9 Node Types** — Input, Output, LLM, Text, API Call, Filter, Transform, Prompt, Note
- **Dynamic Text Node** — Auto-resizes as you type, supports `{{variable}}` syntax to create dynamic input handles
- **DAG Validation** — Automatically checks if your pipeline is a valid Directed Acyclic Graph
- **Clean Dark UI** — Professional dark theme built with React Flow

## Tech Stack

- **Frontend** — React, React Flow
- **Backend** — Python, FastAPI
- **State Management** — Zustand

## Running Locally

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

Open `http://localhost:3000` to view the app.