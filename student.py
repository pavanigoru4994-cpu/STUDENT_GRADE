```python
import csv

FILE_NAME = "student_records.csv"


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 35:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")

    subjects = int(input("Enter Number of Subjects: "))

    total = 0
    fail = False

    for i in range(1, subjects + 1):
        subject = input(f"Enter Subject {i} Name: ")

        while True:
            marks = int(input(f"Enter Marks in {subject}: "))
            if 0 <= marks <= 100:
                break
            print("Marks must be between 0 and 100.")

        if marks < 35:
            fail = True

        total += marks

    average = total / subjects
    grade = calculate_grade(average)
    result = "FAIL" if fail else "PASS"

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            name,
            roll_no,
            total,
            round(average, 2),
            grade,
            result
        ])

    print("\nStudent Record Saved Successfully!")


def view_records():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n========== STUDENT RECORDS ==========")

            for row in reader:
                print(
                    f"Name: {row[0]} | "
                    f"Roll No: {row[1]} | "
                    f"Total: {row[2]} | "
                    f"Average: {row[3]} | "
                    f"Grade: {row[4]} | "
                    f"Result: {row[5]}"
                )

    except FileNotFoundError:
        print("No records found.")


def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            found = False

            for row in reader:
                if row[1] == roll_no:
                    print("\n===== STUDENT FOUND =====")
                    print(f"Name    : {row[0]}")
                    print(f"Roll No : {row[1]}")
                    print(f"Total   : {row[2]}")
                    print(f"Average : {row[3]}")
                    print(f"Grade   : {row[4]}")
                    print(f"Result  : {row[5]}")
                    found = True
                    break

            if not found:
                print("Student not found.")

    except FileNotFoundError:
        print("No records available.")


while True:
    print("\n================================")
    print(" STUDENT GRADE MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View Records")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_records()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank You for Using the System!")
        break

    else:
        print("Invalid Choice.")
```
