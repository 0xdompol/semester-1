
# input() function

Look up documentation on the 'input()' function
- how is the function described?
If a string is passed to input() it is printed to the console without a trailing newline. The function reads a line from input, converts it to a string and returns it  
- what are the inputs? A string
- what is the output? A print statement asking for input, returns inputted string
- think about the description of the data and also the type

Write a small program to test the function
card = input("Enter your card: ")
print(f"Is the {card} your card?")

print("Type something")
user_input = input()
print(f"You typed: {user_input}")