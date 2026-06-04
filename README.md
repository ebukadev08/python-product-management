# 📦 Product Management System

A full-stack CRUD web application built with **FastAPI** (Python) and **React** (JavaScript), backed by **PostgreSQL**.

---

## 🚀 Features

- **Add, Edit, Delete** products with a clean form interface
- **Real-time search** by ID, name, or description
- **Multi-column sorting** (ID, Name, Price, Quantity)
- **Auto-dismissing** success and error notifications
- Responsive layout — works on desktop and mobile

---

## 🛠️ Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Backend   | Python, FastAPI, SQLAlchemy, Pydantic |
| Database  | PostgreSQL                          |
| Frontend  | React, Axios, CSS3                  |
| Dev Tools | Uvicorn, npm                        |

---

## 📁 Project Structure

```
FastApi-Python/
├── backend/
│   ├── main.py             # FastAPI app, routes
│   ├── model.py            # Pydantic schema
│   ├── database.py         # DB engine & session
│   └── database_model.py   # SQLAlchemy ORM model
│
└── frontend/
    ├── src/
    │   ├── App.js
    │   ├── App.css
    │   ├── TaglineSection.js
    │   ├── TaglineSection.css
    │   ├── index.js
    │   └── index.css
    └── package.json
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL running locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Backend setup
```bash
cd backend
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

Update the database URL in `database.py`:
```python
db_url = "postgresql://your_user:your_password@localhost:5433/fastapi_db"
```

Run the backend:
```bash
uvicorn main:app --reload
```

API will be available at `http://localhost:8000`

### 3. Frontend setup
```bash
cd frontend
npm install
npm start
```

App will be available at `http://localhost:3000`

---

## 📡 API Endpoints

| Method | Endpoint          | Description         |
|--------|-------------------|---------------------|
| GET    | `/products`       | Get all products    |
| GET    | `/product/{id}`   | Get product by ID   |
| POST   | `/products`       | Create new product  |
| PUT    | `/products/{id}`  | Update a product    |
| DELETE | `/products/{id}`  | Delete a product    |

---

## 🖼️ Screenshots

> _Add screenshots of your app here_

---

## 👤 Author

**Ebuka**  
Built with 💜 using FastAPI and React

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
