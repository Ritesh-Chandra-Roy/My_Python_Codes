from datetime import datetime 
class Home():
    Company = 'Google'
    @staticmethod
    def print_time():
        now = datetime.now()
        print(f'Time is: {now.strftime("%H:%M:%S")}' )

    @staticmethod
    def greet():
        print("Have A Nice Day!!")
    
    @classmethod #used to overwrite class attributes
    def chngcompany(cls, company):
        cls.Company = company

class Employee(Home):
    Company = 'Alphabate' #will overwrite the base class value for instance of this class
    def __init__(self, role, salary = 10000): #constructor with default argument
        self.role = role #object attribute
        self.salary = salary #object attribute
        
    @property
    def bonus(self):
        return (self.salary)/4
    @property
    def total_salary(self):
        return self.salary + self.bonus
    
    @total_salary.setter
    def total_salary(self, val):
        self.salary = (4*val)/5
    
    @bonus.setter
    def bonus(self, val):
        self.salary = 4*val

    def display(self):
        print(f"salary of employee is: {self.salary}")
        print(f"The role of employee is {self.role}")
        print(f"The Company of employee is {self.Company}")


E = Employee('SDE2')
E.display()
H = Home()
print(H.Company)
H.greet()
E.greet()
H.chngcompany('META')
print(E.total_salary)
E2 = Employee('QAE')
E2.total_salary = 50000
print(E2.salary)
print(E2.bonus)
print(E2.total_salary)
E3 = Employee('SDE2')
E3.bonus = 9000
print(E3.total_salary)