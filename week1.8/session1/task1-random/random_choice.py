import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

num = int(input("Enter the number of names to choose: "))

# Display the chosen names, one per line
n = random.randint(0,1000)
for _ in range(n):
    name_list = random.choices(names,k=n)

