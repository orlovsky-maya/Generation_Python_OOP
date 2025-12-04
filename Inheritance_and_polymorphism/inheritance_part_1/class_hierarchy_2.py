class Shape:
    pass

class Polygon(Shape):
    pass

class Circle(Shape):
    pass

class Quadrilateral(Polygon):
    pass

class Triangle(Polygon):
    pass

class Parallelogram(Quadrilateral):
    pass

class IsoscelesTriangle(Triangle):
    pass

class EquilateralTriangle(Triangle):
    pass

class Rectangle(Parallelogram):
    pass

class Square(Rectangle):
    pass

print(issubclass(Circle, Shape))
print(issubclass(Polygon, Shape))

# valid output
# True
# True

print(issubclass(Triangle, Polygon))
print(issubclass(IsoscelesTriangle, Triangle))
print(issubclass(EquilateralTriangle, Triangle))


# valid output
#
# True
# True
# True