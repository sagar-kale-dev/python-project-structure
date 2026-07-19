## Project Structure

```
expense_tracker/

├── .venv/
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
├── requirements.txt
└── README.md
```
---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Virtual Environment

### Windows (Command Prompt)

```cmd
.venv\Scripts\activate
```

---

## Deactivate Virtual Environment

```bash
deactivate
```

---

## To generate requirement.txt

```cmd
pip freeze > requirement.txt
```

---

## Clone project and run

```cmd
pip install -r requirement.txt
```
