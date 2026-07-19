from app.services.expense_service import ExpenseService
from app.models.expense import Expense
from app.utils.formatter import format_currency

expense_service = ExpenseService()

expense_service.add_expense(Expense("food", 1000))
expense_service.add_expense(Expense("travel", 10000))

all_expenses = expense_service.get_all_expenses()

for expense in all_expenses:
    print(f"Expense : {expense.title} - {format_currency(expense.amount)}")

print(
    f"Total of all expenses: {format_currency(expense_service.calculate_total())}")
