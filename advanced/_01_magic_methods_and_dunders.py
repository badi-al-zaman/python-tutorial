"""
This module demonstrates magic methods (a.k.a. dunder methods) in Python,
such as __init__, __str__, and __len__.
"""


class Vector:
    """
    A simple 2D vector class demonstrating magic methods (dunders).
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        return NotImplemented

    def __len__(self):
        return 2  # Vectors are always 2-dimensional

    def __call__(self, *args, **kwargs):
        return Vector(self.x, self.y)


v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2)  # Vector(7, 10)
print(v1 - v2)  # Vector(-3, -4)
print(v1)  # (2, 3)
print(repr(v2))  # Vector(5, 7)
print(v1 == v2)  # False
print(v1 < v2)  # True
print(len(v1))  # 2

print(v1())  # (2, 3)
