
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
city_a_temp = [22, 24, 23, 25, 26, 27, 24]
city_b_temp = [20, 21, 22, 21, 23, 24, 22]

plt.figure(figsize=(8,5))
plt.plot(days, city_a_temp, marker='o', label='City A')
plt.plot(days, city_b_temp, marker='s', label='City B')
plt.title('Temperature Comparison: City A vs City B')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()
