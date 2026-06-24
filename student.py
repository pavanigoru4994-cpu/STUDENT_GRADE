```python
# Student Grade Management System

print("===================================")
print("   STUDENT GRADE MANAGEMENT SYSTEM")
print("===================================")

# Student Details
student_name = input("Enter Student Name: ")

# Number of subjects
subjects = int(input("Enter Number of Subjects: "))

total_marks = 0
fail = False

# Enter marks
for i in range(1, subjects + 1):
    marks = int(input(f"Enter Marks for Subject {i}: "))

    if marks < 35:
        fail = True

    total_marks += marks

# Calculate average
average = total_marks / subjects

# Determine Grade
if fail:
    grade = "FAIL"
elif average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "FAIL"

# Display Result
print("\n===== STUDENT REPORT =====")
print("Student Name :", student_name)
print("Total Marks  :", total_marks)
print("Average      :", round(average, 2))
print("Grade        :", grade)
print("==========================")
```
