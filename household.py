import pandas as pd
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]
expense_series = pd.Series(expenses, index=categories)
print("Household Expenses:")
print(expense_series)
print("\nTotal Monthly Expense:", expense_series.sum())
print("Maximum Expense Category:", expense_series.idxmax())
