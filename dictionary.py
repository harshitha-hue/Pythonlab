students = {
    "Abhishek": 85,
    "Bharath": 92,
    "shekar": 78,
    "Diana": 90,
    "preethi": 88
}

name = input("Enter the student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print(f"No record found for student named '{name}'.")
