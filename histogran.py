import matplotlib.pyplot as plt
import numpy as np

ages = np.random.randint(10, 70, 100)

plt.hist(ages, bins=10, color='orange', edgecolor='black')
plt.title("Age Distribution of 100 People")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.show()
