import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("You must specify either radius or diameter")
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area:.2f})"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("You can only add two Circle instances")
    
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        raise TypeError("You can only compare two Circle instances")
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        raise TypeError("You can only compare two Circle instances")
    
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        raise TypeError("You can only compare two Circle instances")

# Example usage:
circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)

print(circle1)  # Output: Circle(radius=5, diameter=10, area=78.54)
print(circle2)  # Output: Circle(radius=5.0, diameter=10, area=78.54)

circle3 = circle1 + circle2
print(circle3)  # Output: Circle(radius=10.0, diameter=20.0, area=314.16)

print(circle1 > circle2)  # Output: False
print(circle1 == circle2) # Output: True

# Sorting a list of circles:
circles = [Circle(radius=3), Circle(diameter=14), Circle(radius=1)]
circles.sort()
for c in circles:
    print(c)
# Output:
# Circle(radius=1, diameter=2, area=3.14)
# Circle(radius=3, diameter=6, area=28.27)
# Circle(radius=7.0, diameter=14, area=153.94)

#Part II

def draw_circle(circle, turtle_instance):
    turtle_instance.penup()
    turtle_instance.goto(0, -circle.radius)
    turtle_instance.pendown()
    turtle_instance.circle(circle.radius)

def draw_sorted_circles(circles):
    screen = turtle.Screen()
    t = turtle.Turtle()
    
    for circle in circles:
        draw_circle(circle, t)
    
    screen.mainloop()

# Example usage:
circles = [Circle(radius=30), Circle(radius=50), Circle(radius=10)]
circles.sort()
draw_sorted_circles(circles)
