N = int(input("enter the subjects -"))
total = 0
for _ in range(N):
    total += int(input())
average = total / N
if average >= 85:
    grade = "Excellent"
elif average >= 60:
    grade = "Good"
elif average >= 40:
    grade = "Average"
else:
    grade = "Fail"
print(f"Average: {average}")
print(f"Grade: {grade}")
 