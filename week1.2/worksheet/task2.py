# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
numbers = read_numbers()
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)
temp = numbers
temp.sort()
if len(numbers) % 2 == 1:
    median = numbers[int(len(numbers) / 2)]
else:
    mid1 = numbers[(len(numbers) // 2) - 1]
    mid2 = numbers[(len(numbers) // 2)]
    median = (mid1 + mid2) / 2
print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")