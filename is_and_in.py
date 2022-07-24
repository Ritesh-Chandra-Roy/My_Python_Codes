


list_a = [20, 30 , 40]
list_b = [20, 30 , 40]

if(list_a == list_b):
    print(True)
else: 
    print(False)
# On the Other Hand

if(list_a is list_b): #here the condition is flase because both operands does not refer to same object
    print(True)
else:
    print(False)

list_c = list_a # Since here list_c is created directly from list_a therefore the condition is true

if(list_a is list_c):
    print(True)
else:
    print(False)

# in Operator
print(20 in list_a) #this will print true as 20 is present in list_a....in operator Used mostly in for loop for iteration
comment = input("Enter comment: ")
flag = False
if("Make a lot of money" in comment):
    flag = True
elif("Buy now" in comment):
    flag = True
else:
    print("Not a Spam!!")
if(flag == True):
    print("Spam Comment!!")