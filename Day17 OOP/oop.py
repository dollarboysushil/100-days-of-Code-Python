#from YT Tech with Tim


class Circle:
    
    def __init__(self , radius):
        self.radius = radius
        
        
    def area(self):
        return self.radius * self.radius * 3.14
    
    def perimeter(self):
        return self.radius * 3.14 * 2
    
    
c1 = Circle(4)
print(c1.area())
