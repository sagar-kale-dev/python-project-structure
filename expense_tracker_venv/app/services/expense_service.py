from app.data.expenses import expenses


class ExpenseService:
    def add_expense(self, expense):
        expenses.append(expense)

    def get_all_expenses(self):
        return expenses

    def calculate_total(self):
        total = 0

        for expense in expenses:
            total += expense.amount

        return total
