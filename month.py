
monthly_expenses = {
    "January": 1200,
    "February": 1100,
    "March": 1150,
    "April": 1300,
    "May": 1250,
    "June": 1400,
    "July": 1350,
    "August": 1250,
    "September": 1200,
    "October": 1300,
    "November": 1100,
    "December": 1500
}
total_expense = sum(monthly_expenses.values())

print("Monthly Expenses:")
for month, amount in monthly_expenses.items():
    print(f"{month}: ${amount}")

print(f"\nTotal Yearly Expense: ${total_expense}")
