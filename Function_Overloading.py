def add(*args):
    answer = 0
    for x in args:
        answer = answer + x
    print(answer)


add(5, 6)
add(6, 5, 11.3, 10.0458)
add(1)
 #Second Method(Better One)
from multipledispatch import dispatch
  
@dispatch(int,int)
def product(first,second):
    result = first*second
    print(result)
  

@dispatch(int,int,int)
def product(first,second,third):
    result  = first * second * third
    print(result)
  

@dispatch(float,float,float)
def product(first,second,third):
    result  = first * second * third
    print(result)
  
  

product(2,3,2)
product(2.2,3.4,2.3)