
# function implementation
from typing import List

def rectangle_area(length: int, width: int) -> int:  # define suitable input data
    """ Takes length and width as integers and calculates the area of a rectangle, returning an integer """       # implement the function
    area = length * width
    return area              # return an appropriate value

def even_list(integer: int) -> int:
    """
    Takes integer as input and outputs a list of even integers that exist
    between 0 and the inputted value 
    """
    even_list = []
    for i in range(0, integer, 2):
        even_list.append(i)
    return even_list

def mean_list(int_list: list[int]) -> list[int]:
    """ Takes a list with integers as input and calculates the mean of that list, returning a float"""
    mean = sum(int_list) / len(int_list)
    return mean

# testing the function

print(f"Area is {rectangle_area(5,10)}")   # provide suitable data matching your inputs
print(f"Even integer list is {even_list(67)}")
my_list = [1, 109, 5, 700, 67, 3457, 5]
print(f"Mean of the list is {mean_list(my_list)}")