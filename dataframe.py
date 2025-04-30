import pandas as pd
data = {
    'Employee': ['John', 'Alice', 'Bob', 'Emma'],
    'Department': ['IT', 'HR', 'Finance', 'IT'],
    'Salary': [60000, 55000, 70000, 72000],
    'Age': [30, 28, 35, 32]
}

df = pd.DataFrame(data)
print("First two rows of the DataFrame:")
print(df.head(2))
df['Experience'] = [5, 3, 7, 6]

print("\nDataFrame after adding the 'Experience' column:")
print(df)
average_salary = df['Salary'].mean()
print(f"\nAverage salary of all employees: {average_salary}")
students_data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma'],
    'Math': [85, 70, 90, 78],
    'Science': [88, 92, 76, 85],
    'English': [75, 80, 90, 88]
}
students_df = pd.DataFrame(students_data)
students_above_80_in_math = students_df[students_df['Math'] > 80]
print("\nStudents who scored more than 80 in Math:")
print(students_above_80_in_math)
sorted_by_science = students_df.sort_values(by='Science', ascending=False)
print("\nStudents sorted by Science scores in descending order:")
print(sorted_by_science)
highest_english_score = students_df.loc[students_df['English'].idxmax()]
print("\nStudent with the highest English score:")
print(highest_english_score)
