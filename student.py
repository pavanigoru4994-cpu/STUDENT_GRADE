```python
# Student Grade Management System - Level 2

def get_student_data():
    name = input("Enter Student Name: ")
    subjects = int(input("Enter Number of Subjects: "))

    total_marks = 0
    fail = False

    for i in range(1, subjects + 1):
        marks = int(input(f"Enter Marks for Subject {i}: "))

        if marks < 35:
            fail = True

        total_marks += marks

    average = total_marks / subjects

    return name, total_marks, average, fail


def calculate_grade(average, fail):
    if fail:
        return "FAIL"
    elif average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "FAIL"


def display_report(name, total_marks, average, grade):
    print("\n===================================")
    print("      STUDENT GRADE REPORT")
    print("===================================")
    print(f"Student Name : {name}")
    print(f"Total Marks  : {total_marks}")
    print(f"Average      : {average:.2f}")
    print(f"Grade        : {grade}")
    print("===================================")


# Main Program
name, total_marks, average, fail = get_student_data()
grade = calculate_grade(average, fail)
display_report(name, total_marks, average, grade)
```
