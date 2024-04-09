#object oreinted programmings

# class Students():
#                     def __init__(self,name): #constructor
#                                         self.name=name
#                                         print("Constructor Called!")
                    

# s=Students("Ankit Kumar")
# print(s.name)

class Students:
                    def __init__(self,name,marks):
                                        self.name=name
                                        self.marks=marks
                                        
                    def average(self):
                                        sum=0
                                        for el in self.marks:
                                                            sum+=el
                                        print("Name:",self.name)
                                        print("Marks:",sum/3)

s=Students("Ankit",[80,85,70])
s.name="Rahul "
s.average()
