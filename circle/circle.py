import math

class Circle:

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radius = radius

    def get_radius(self):
        return self.radius
    tete
    def set_radius(self,radius):
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2 
    
    def get_perimeter(self):
        return math.pi * self.radius * 2
    
    def __mul__(self, n):
        if n <= 0:
            raise ValueError("El multiplicador debe ser mayor a 0")
        return Circle(self.radius * n) 

    def __str__(self):
        return f"El Radio del Circulo es de {self.radius}"
