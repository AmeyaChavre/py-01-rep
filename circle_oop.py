class Circle():
    
    pi = 3.14159652
    
    def __init__(self,radius=1):
        self.radius = radius
    
    def get_circumference(self):
        return 2 * Circle.pi * self.radius
    
    def get_area(self):
        return Circle.pi * self.radius **2
    
    def print_func(self):
        print(f'The circumference of the circle is {self.get_circumference()} and the area is {self.get_area()}')

circle_object = Circle(3)
circle_object.print_func()
