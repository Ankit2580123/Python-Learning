#implement addition of complex number using polymorphism
class Complex:
                    def __init__(self,real,img):
                                        self.real=real
                                        self.img=img
                    
                    def print(self):
                                        print(self.real,"i","+", self.img,"j")
                                        
                    def __add__(self,num2):  #creating a dunder function
                                        newreal=self.real+num2.real
                                        newimg=self.img+num2.img
                                        return Complex(newreal,newimg)

                    def __sub__(self,num2):  #creating a dunder function
                                        newreal=self.real-num2.real
                                        newimg=self.img-num2.img
                                        return Complex(newreal,newimg)

num1=Complex(5,10)
num1.print()

num2=Complex(10,6)
num2.print()

# num3=num1.add(num2)
# num3.print()
addNum=num1+num2 
subNum=num1-num2
addNum.print()
subNum.print()