# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height
        if type(self.width) != int:
            raise TypeError("width must be an integer")
        elif self.width <= 0:
            raise ValueError("width must be greater than 0")
        if type(self.height) != int:
            raise TypeError("height must be an integer")
        elif self.height <= 0:
            raise ValueError("height must be greater than 0")

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

    def is_square(self):
        """
        Returns True if the rectangle is a square, False otherwise.
        """
        return True if self.width == self.height else False

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

rect = Rectangle(5, 6)
perimeter = rect.perimeter()
print(f"Perimeter: {perimeter}")  # Output: Perimeter: 22