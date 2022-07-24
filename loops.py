i = 0
while i<10:
    print("Iteration ", i)
    i += 1
print("Done!")
fruits = ['Guava', 'Apple', 'Mango', 'Litchi', 'Grapes']
# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i += 1
for item in fruits:
    print(item)
# Range Function
 
# for i in range(10, 20, 2): #u can exclude the last argument if step size not needed
#     print(i)
for item in fruits:
    if(item=='Kiwi'):
        print("Found!")
        break
else: print("Loop not broken!")

for item in fruits:
    if(item=='Apple'):
        continue #will not execute the body and go to next iteration
    print(item)

num =int(input("Enter the number: "))
for i in range(2, int(num/2)):
    if(num%i==0):
        print("Not a Prime Number!!")
        break
else: print("Its a prime number!!")

d = {'x': 1, 'y': 2, 'z': {'a':10, 'b': 20, 'c': 30}}

for key in d:
    print(key, 'corresponds to', d[key])