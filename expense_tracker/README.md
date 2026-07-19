# Expense Tracker

A simple Python Expense Tracker project created to practice:

- Python project structure
- Modules and packages
- Object-oriented programming
- Separation of responsibilities

No framework or database is used. The focus is understanding clean application organization.

---

## Project Structure

```
expense_tracker/

├── app/
│   ├── main.py
│   │
│   ├── models/
│   │   └── expense.py
│   │
│   ├── services/
│   │   └── expense_service.py
│   │
│   ├── data/
│   │   └── expenses.py
│   │
│   └── utils/
│       └── formatter.py
│
├── tests/
│
└── README.md
```

---

## Folder Purpose

### main.py

Application entry point.

Responsible for:

- Starting the program
- Creating objects
- Calling services

---

### models/

Contains data objects.

Example:

```
expense.py
```

Defines what an Expense looks like.

---

### services/

Contains application logic.

Example:

```
expense_service.py
```

Handles:

- Adding expenses
- Getting expenses
- Calculating totals

---

### data/

Stores application data.

Currently uses an in-memory Python list.

Later it can be replaced with:

- SQLite
- PostgreSQL
- MongoDB

---

### utils/

Contains reusable helper functions.

Example:

- Currency formatting
- Date formatting

---

## Run Application

Recommended:

```bash
python -m app.main
```

This runs `main.py` as a module.
