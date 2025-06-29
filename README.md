# Superheroes API

A Restful API built with Flask and SqlAlchemy that manages a collectection of superheroes, their powers, and the relationships between them. It supports full CRUD operations, validation, and relational data handling.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Database Models](#database-models)
- [Available Endpoints](#available-endpoints)
- [Validate Rules](#validate-rules)
- [Future Improvements](#future-improvements)

---

#Project Description

This API allows users to:
- View all heroes and individual hero details
- View all powers and individual power details 
- Update a power's description
- Assign powers toheroes with strength levels

It demonstrates core backend skills using Flask, SqlAlchemy ORM, and proper REST API design patterns.

---

#Technologies Used

- Python 3.12
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (as the database)

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EmmanuelNgetich637/superheroes-api.git
   cd superheroes-api

2. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate

3. **Install dependencies:**
```bash
pip install -r requirements.txt

4. **Run migrations:**
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. **Seed the database:**
```bash
flask run

#Author 
Emmanuel Ng'etich
