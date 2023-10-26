import math

class Circle:

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radius = radius