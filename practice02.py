class Employee:
                    def __init__(self,role,dept,salary):
                                        self.role=role
                                        self.dept=dept
                                        self.salary=salary
                    def show_details(self):
                                        print("Role:",self.role)
                                        print("Department:",self.dept)
                                        print("Salary:",self.salary)
                                        
class Engineer(Employee):
                    def __init__(self,name,age):
                                        self.name=name
                                        self.age=age
                                        super().__init__("Software Engineer","IT","50,000")
                                        
                    


eng=Engineer("Ankit",23)
eng.show_details()
                                        