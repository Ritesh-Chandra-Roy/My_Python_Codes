ls = [i for i in range(10)]
print(ls)

for index, item in enumerate(ls):
    if index ==2 or index == 5 or index == 7:
        print(index, item)
