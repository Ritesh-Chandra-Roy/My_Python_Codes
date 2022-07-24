from datetime import datetime 

class Employee:
    Company = 'Google' #class attribute
    def __init__(self, role, salary = 10000): #constructor with default argument
        self.role = role #object attribute
        self.salary = salary #object attribute

    def display(self):
        print(f"salary of employee is: {self.salary}")
        print(f"The role of employee is {self.role}")
        print(f"The Company of employee is {self.Company}")

    @staticmethod
    def print_time():
        
        now = datetime.now()
        print(f'Time is: {now.strftime("%H:%M:%S")}' )

    @staticmethod
    def greet():
        print("Have A Nice Day!!")

Employee.print_time()
Roy = Employee('Intern')
Jay = Employee('SDE2', 50000)
# print(Roy.Company)
# print(Jay.Company) 
# Roy.Company = 'Microsoft' #will overwrite the class attribute for Roy instance only
# print(Roy.Company)
# print(Jay.Company)
# Roy.display()
Jay.display()
# The above two function calls are equivalent to below
Employee.display(Roy)
Employee.greet()