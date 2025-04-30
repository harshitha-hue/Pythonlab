import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [30, 32, 31, 29, 35, 36, 34]

plt.plot(days, temperatures, marker='o', color='blue')
plt.title("Temperature Over 7 Days")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
