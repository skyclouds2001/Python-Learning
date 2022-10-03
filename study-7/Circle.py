import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def get_perimeter(self):
        return math.pi * 2 * self.radius

    def get_area(self):
        return math.pi * self.radius * self.radius

    def set_radius(self, radius):
        self.radius = radius
