import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History", "Art"]
marks = [88, 92, 85, 78, 90]

plt.bar(subjects, marks, color='green')
plt.title("Marks in 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.show()
