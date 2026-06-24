```python
# Student Grade Management System - Level 3

def get_student_data():
    name = input("Enter Student Name: ")
    subjects = int(input("Enter Number of Subjects: "))

    marks_list = []
    total_marks = 0

    for i in range(1, subjects + 1):
        subject_name = input(f"Enter Subject {i} Name: ")

        while True:
            marks = int(input(f"Enter Marks for {subject_name}: "))

            if 0 <= marks <= 100:
                break

            print("Invalid Marks! Please enter marks between 0 and 100.")

        marks_list.append((subject_name, marks))
        total_marks += marks

    average = total_marks / subjects

    return name, marks_list, total_marks, average


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 35:
        return "D"
    else:
        return "F"


def check_result(marks_list):
    for subject, marks in marks_list:
        if marks < 35:
            return "FAIL"
    return "PASS"


def display_report(name, marks_list, total_marks, average, grade, result):
    print("\n====================================")
    print("      STUDENT GRADE REPORT")
    print("====================================")

    print(f"Student Name : {name}")

    print("\nSubject-wise Marks:")
    for subject, marks in marks_list:
        print(f"{subject:<15} : {marks}")

    print("\n------------------------------------")
    print(f"Total Marks   : {total_marks}")
    print(f"Average Marks : {average:.2f}")
    print(f"Grade         : {grade}")
    print(f"Result        : {result}")
    print("====================================")


# Main Program
name, marks_list, total_marks, average = get_student_data()

grade = calculate_grade(average)
result = check_result(marks_list)

display_report(
    name,
    marks_list,
    total_marks,
    average,
    grade,
    result
)
```
