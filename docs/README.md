
# Geometric Shapes Calculation Documentation

This document provides an overview and examples of using Python modules to calculate the area and perimeter of various geometric shapes: circles, rectangles, squares, and triangles.

## Circle

### Code:
```python
from math import pi

def circle_area(r):
    """
    Calculate the area of a circle.

    Parameters:
    r (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return pi * r * r

def circle_perimeter(r):
    """
    Calculate the perimeter of a circle.

    Parameters:
    r (float): The radius of the circle.

    Returns:
    float: The perimeter of the circle.
    """
    return 2 * pi * r

# For a circle with radius 5
circle_radius = 5
example_circle_area = circle_area(circle_radius)
example_circle_perimeter = circle_perimeter(circle_radius)

print("Area:", example_circle_area)
print("Perimeter:", example_circle_perimeter)
```

### Results:
- **Area:** 78.54 units²
- **Perimeter:** 31.42 units

## Rectangle

### Code:
```python
def rectangle_area(a, b):
    """
    Calculate the area of a rectangle.

    Parameters:
    a (float): The length of the rectangle.
    b (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return a * b

def rectangle_perimeter(a, b):
    """
    Calculate the perimeter of a rectangle.

    Parameters:
    a (float): The length of the rectangle.
    b (float): The width of the rectangle.

    Returns:
    float: The perimeter of the rectangle.
    """
    return (a + b) * 2

# For a rectangle with length 10 and width 5
rectangle_length = 10
rectangle_width = 5
example_rectangle_area = rectangle_area(rectangle_length, rectangle_width)
example_rectangle_perimeter = rectangle_perimeter(rectangle_length, rectangle_width)

print("Area:", example_rectangle_area)
print("Perimeter:", example_rectangle_perimeter)
```

### Results:
- **Area:** 50 units²
- **Perimeter:** 30 units

## Square

### Code:
```python
def square_area(a):
    """
    Calculate the area of a square.

    Parameters:
    a (float): The side length of the square.

    Returns:
    float: The area of the square.
    """
    return a * a

def square_perimeter(a):
    """
    Calculate the perimeter of a square.

    Parameters:
    a (float): The side length of the square.

    Returns:
    float: The perimeter of the square.
    """
    return 4 * a

# For a square with side length 6
square_side_length = 6
example_square_area = square_area(square_side_length)
example_square_perimeter = square_perimeter(square_side_length)

print("Area:", example_square_area)
print("Perimeter:", example_square_perimeter)
```

### Results:
- **Area:** 36 units²
- **Perimeter:** 24 units

## Triangle

### Code:
```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle.

    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return a * h / 2

def triangle_perimeter(a, b, c):
    """
    Calculate the perimeter of a triangle.

    Parameters:
    a (float): The length of side a of the triangle.
    b (float): The length of side b of the triangle.
    c (float): The length of side c of the triangle.

    Returns:
    float: The perimeter of the triangle.
    """
    return a + b + c

# For a triangle with base 10, height 5, and sides 5, 6, and 7
triangle_base = 10
triangle_height = 5
triangle_side_a = 5
triangle_side_b = 6
triangle_side_c = 7
example_triangle_area = triangle_area(triangle_base, triangle_height)
example_triangle_perimeter = triangle_perimeter(triangle_side_a, triangle_side_b, triangle_side_c)

print("Area:", example_triangle_area)
print("Perimeter:", example_triangle_perimeter)
```

### Results:
- **Area:** 25 units²
- **Perimeter:** 18 units

# Commit Log

- `69e8e473` Add docstrings to circle.py functions


- `3a5796a` Refactor rectangle.py: Add docstrings to area() and perimeter() functions


- `cb77247` Add area and perimeter comments to square.py


- `7c49408` Added comments to triangle.py functions

