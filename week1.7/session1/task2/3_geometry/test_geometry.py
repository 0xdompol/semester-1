# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

import math

from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    
    # complete the implementation for
    # testing distance_to()
def test_distance_to():
    p1 = Point(3,5)
    p2 = Point(-8,-7)
    assert p1.distance_to(p2) == math.hypot(11,12)
    assert Point(0,0).distance_to(Point(-6,6)) == math.hypot(6,6)
    

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates

def test__init__circle():
    c = Circle(5)
    assert c.radius == 5
    assert c.centre.x == 0.0
    assert c.centre.y == 0.0

def test_area_circle():
    c = Circle(3)
    assert c.area() == math.pi * 3 * 3

def test_perimeter_circle():
    c = Circle(4)
    assert c.perimeter() == 2 * math.pi * 4