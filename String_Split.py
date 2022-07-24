
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gamil.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0] #the split function returns a list of words in the string
        print(names)
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


emp1 = Employee("emp", "1")
print(emp1.email)
roy = Employee(None, None )
roy.email = 'rc.roy@gmail.com'
print(roy.fname)
print(roy.lname)
# o = "this is a string"
# print(dir(skillf))
# print(id("that that"))

# import inspect
# print(inspect.getmembers(skillf))


