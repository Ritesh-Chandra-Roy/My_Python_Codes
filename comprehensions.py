# output_list = [output_exp for var in input_list if (var satisfies this condition)]

ls = [i for i in range(50) if i%5==0]
print(ls)
dict1 = {i:f"Item {i}" for i in range(5)}
#Reversing ket value pair in Dictionary
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n", dict2)
ls2 =[7, 4, 9, 4, 11, 9, 7 , 9, 11]
set1 = {value for value in ls2} #generating a set from list using comprehension
print(set1)
num = int(input("Enter a number: "))
table  = [i*num for i in range(1,11)]
print(table)
evens = [i%2==0 for i in range(10)] #Generator comrihension
print(evens)
print(evens.__next__())

print(evens.__next__())