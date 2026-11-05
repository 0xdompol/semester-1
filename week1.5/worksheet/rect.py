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
        if self.width.isinstance(int) == False:
            raise TypeError("width must be an integer")
        else:
            if self.height.isinstance(int) == False:
                raise TypeError("height must be an integer")

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
