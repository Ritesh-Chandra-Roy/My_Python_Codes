while(True):
    a = input("Enter a number: ")
    if a =='q':
        break
    try:
        a = int(a)
        if a>6:
            print("Number entered greater than six!")
    except Exception as e:
        print(f"Wrong Input...Input Number ")
    finally:
        print("Inside Finally...Ye execute hoga ho hoga!!")

print("Game Over!")



# try:
#     a = int(input("Enter a number: "))
#     c = 1/a
#     print(c)
# except ValueError as e:
#     print("Value Error Exception Occured!! ")

# except ZeroDivisionError as e:
#     print("Make sure not dividing by zero!!")


# def incriment(num):
#     try:
#         return int(num) + 1
#     except:
#         raise ValueError("Invalid Value!!")
#     # else:
#     #     print("Number incrimented succesfully")

# a  = incriment('fdf2')
# print(a)

def incriment(num):
    try:
     num = int(num) + 1
    except Exception as e:
        print("Invalid Value!!")
    else:
        print("Number incrimented succesfully!!")
        return num
a  = incriment('sd')
print(a)