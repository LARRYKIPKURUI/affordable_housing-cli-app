#  Affordable Housing CLI System

A command-line interface (CLI) application for managing agents, clients, houses, and their relationships in a real estate system. Built with Python and SQLAlchemy.

---

##  Project Structure

```
affordable_housing/
├── lib/
│   ├── cli.py           # CLI entry point
│   ├── helpers.py       # Business logic & DB operations
│   ├── models.py        # SQLAlchemy ORM models
│   ├── debug.py         # DB setup and session creation
├── my_database.db       # SQLite database 
├── README.md
```

---

##  Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/LARRYKIPKURUI/affordable_housing-cli-app.git>
   cd affordable_housing
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # this is for Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install Pipfile
   ```

4. **Run the app**:
   ```bash
   python lib/cli.py
   ```

---

##  Features

- -> Add/List/Delete Agents
- -> Add/List Clients
- -> Add/List Houses
- -> Assign an Agent to a Client for a House
- -> Timestamped records with UTC timezone
- -> SQLite database with relationships

---

##  Models Overview and Demo Presentation

To Check or Have an overview of the database schema find it  through this link [https://dbdiagram.io/d/Affordable-Housing-683459d46980ade2eb6923b7 ] -> [Database Schema]


## Demo of How the project works
Find below the link for a demo made to show the working of the project  
[https://www.loom.com/share/c10c70a825f14b2cabb813fe5b0639e7?sid=507a3c89-e1e8-427b-9d04-7d0dca3c0975] -> [Demo ]