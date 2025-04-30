
days = list(range(1, 31))
product_a_sales = np.random.randint(80, 150, size=30)
product_b_sales = np.random.randint(60, 130, size=30)


plt.figure(figsize=(10,5))
plt.plot(days, product_a_sales, label='Product A', marker='o')
plt.plot(days, product_b_sales, label='Product B', marker='s')
plt.title('Sales Comparison: Product A vs Product B (Monthly)')
plt.xlabel('Day of Month')
plt.ylabel('Sales Units')
plt.legend()
plt.grid(True)
plt.show()
