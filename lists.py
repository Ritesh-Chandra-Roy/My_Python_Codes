arr = [7, 4, 9, 11, 29, 50, 44, 25]
print(arr[1])
print(sum(arr))
arr[5] = 100
print(arr)
#list in python can have items of different typse
arr2 = ["Roy", 20, 66, "India", 66]
print(arr2)
# slicing also works for lists
#methods:-
arr.sort()
print("Sorted List: ", arr)
arr.reverse()
print("Reversed list: ", arr)
arr.append(20)
arr.insert(1, 10) #insert 10 at index 1
print(arr)
arr.pop(2) #delete item at 2nd index
arr.remove(100)
print(arr)
# https://docs.python.org/3/tutorial/datastructures.html for more methods