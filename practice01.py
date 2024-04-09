'''practice01==> Create a class circle and inialize the radius using constructor 
and make two methodes whose calculate area and perimeter'''

class Circle:
                    pie=3.14
                    def __init__(self,radius):
                                        self.radius=radius
                                        
                    def area(self):
                                        area=self.pie*(self.radius**2)
                                        return area
                                        
                                        
                    def perimeter(self):
                                        perimeter=2*self.pie*self.radius
                                        return perimeter
radius=int(input("Enter the radius: "))
c=Circle(radius)
area=c.area()
perimeter=c.perimeter()
print("Area of Circle:",area)
print("Perimeter of Circle:",perimeter)
