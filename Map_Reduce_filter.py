from functools import reduce

def square(n):
    return n*n



numbers  = ["7", "4", "9", "11", "29"]
print(numbers)
numbers = list(map(int, numbers))
print(numbers)
sq_lis = list(map(square, numbers))
print(sq_lis)

sum = reduce(lambda x, y:x+y, numbers)
print(sum)
ls2 = list(filter(lambda x: x>7, numbers))
print(f"Ls2 from filter: {ls2}")

maximum = reduce(max, ls2)
print(f"max: {maximum}")
# sum2 = reduce(square, numbers)
# print(sum2)
print(str.upper('gillu'))
