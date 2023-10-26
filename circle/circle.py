import math

class Circle:

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self,radius):
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radius = radius

    def get_area(self):
        return 3.14159 * self.radius**2 
    
    def get_perimeter(self):
        return 3.14159 * self.radius * 2
    
    def __mul__(self, n):
        if n <= 0:
            raise ValueError("El multiplicador debe ser mayor a 0")
        return Circle(self.radius * n) 

    def __str__(self):
        return f"El Radio del Circulo es de {self.radius}"
