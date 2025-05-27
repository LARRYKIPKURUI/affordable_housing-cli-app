# Database & Migrations Guide — Affordable Housing CLI

This guide explains how the database works, how to create and manage it, and how to handle migrations in the **Affordable Housing CLI** project.

---

## Database Stack

- **Database Engine**: SQLite (lightweight & file-based)
- **ORM**: SQLAlchemy
- **Schema Management**: Manual / optional Alembic setup

---

## Project DB Structure

```
affordable_housing/
├── lib/
│   ├── models.py       # SQLAlchemy ORM models
│   ├── debug.py        # Creates DB & session (run this first)
├── my_database.db      # Auto-generated SQLite file
```

---

## Setting Up the Database

1. **Create tables using the models**:
   In `debug.py`, the tables are created when you run the file.

   ```bash
   python lib/debug.py
   ```

   This does the following:
   - Connects to SQLite using `create_engine`
   - Binds a session
   - Creates all tables via `Base.metadata.create_all(engine)`



## Optional: Alembic for Migrations 

To support versioned migrations:

1. **Install Alembic**:
   ```bash
   pip install alembic
   ```

2. **Initialize Alembic**:
   ```bash
   alembic init migrations
   ```

3. **Edit `alembic.ini` and `env.py`**:
   - Point `sqlalchemy.url` to `sqlite:///my_database.db`
   - Import `Base` from your models module

4. **Generate migration**:
   ```bash
   alembic revision --autogenerate -m "Initial tables"
   ```

5. **Apply migration**:
   ```bash
   alembic upgrade head
   ```

_Note: This is optional — basic usage doesn't require Alembic._

---

## 📌 Default Tables

- `agents`
- `clients`
- `houses`
- `agents_clients` (junction table)

All include `created_at` timestamps (UTC) by default.

---

## 🔁 Seeding Data

You can seed test data using helper functions or directly through `seed.py`:
