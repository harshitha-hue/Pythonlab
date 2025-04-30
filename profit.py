
sales = [100, 150, 200, 250, 300, 350, 400]
profit = [20, 35, 50, 65, 80, 100, 120]

plt.figure(figsize=(7,5))
plt.scatter(sales, profit, c='green', edgecolor='black')
plt.title('Sales vs Profit')
plt.xlabel('Sales ($)')
plt.ylabel('Profit ($)')
plt.grid(True)
plt.show()
