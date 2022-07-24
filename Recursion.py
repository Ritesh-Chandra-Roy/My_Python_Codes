import re


def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))
def sum(n):
    if(n == 0):
        return 0
    return n+sum(n-1)

print(sum(10))

def Table(num, i=1):
    if i>10:
        return 
    print(f"{num} X {i} = {num*i}")
    Table(num, i+1)

Table(19)