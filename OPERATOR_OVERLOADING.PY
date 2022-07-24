


class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num2): #dunder method predefined in python to overload + operator
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2): #dunder method predefined in python to overload * operator
        print('lets multiply')
        return self.num * num2.num
    
    def __str__(self):  #dunder method predefined in python to overload print operator
        return f"Number = {self.num}"

n1 = Number(6)
n2 = Number(7)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)
print(n1)