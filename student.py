students = []
def create_students():
    global students
    students = [
        ("Alan", 101, (85, 90, 78), "B"),
        ("Bunny", 102, (88, 76, 92), "A"),
        ("Charls", 103, (70, 65, 60), "C")
    ]
def display_all_students():
    if not students:
        print("No student records available.")
    for student in students:
        print(f"Name: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}, Grade: {student[3]}")
def add_student(name, roll_no, marks, grade):
    students.append((name, roll_no, marks, grade))
    print(f"Student {name} added successfully.")
def search_student(roll_no):
    for student in students:
        if student[1] == roll_no:
            print(f"Found: Name: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}, Grade: {student[3]}")
            return
    print("Student not found.")
def calculate_total_marks():
    for student in students:
        total = sum(student[2])
        print(f"Name: {student[0]}, Roll No: {student[1]}, Total Marks: {total}")
def update_grade(roll_no, new_grade):
    global students
    updated = False
    for i in range(len(students)):
        if students[i][1] == roll_no:
            student = students[i]
            students[i] = (student[0], student[1], student[2], new_grade)
            updated = True
            print(f"Grade updated for Roll No {roll_no}.")
            break
    if not updated:
        print("Student not found.")
def remove_student(roll_no):
    global students
    for i in range(len(students)):
        if students[i][1] == roll_no:
            removed = students.pop(i)
            print(f"Removed student: {removed[0]}")
            return
    print("Student not found.")

if __name__ == "__main__":
    create_students()
    print("Initial Student Records:")
    display_all_students()

    print("\nAdding a New Student:")
    add_student("David", 104, (91, 82, 77), "B")

    print("\nSearching for Student with Roll No 102:")
    search_student(102)

    print("\nTotal Marks of All Students:")
    calculate_total_marks()

    print("\nUpdating Grade for Roll No 103:")
    update_grade(103, "B+")

    print("\nRemoving Student with Roll No 101:")
    remove_student(101)

    print("\nFinal Student Records:")
    display_all_students()
