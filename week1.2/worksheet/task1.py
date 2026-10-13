# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Enter an integer grade in the range 0-100: ")
try:
    grade = int(grade)
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")
if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")
elif grade < 40:
    print(f"{grade} is a Fail")
elif grade < 70:
    print(f"{grade} is a Pass")
else:
    print(f"{grade} is a Distinction")