age = int(input('Enter Your Age: '))
if(age >= 17 and age < 21):
    print('Eligible')
elif(age==21):
    print('Eligible for Special Quota')
else:
    print("Not Eligible")


username = input("Enter Username(max 10 characters): ")

length = len(username)

if(length>10):
    print("More than 10 characters not allowed!!")
else:
    print("Valid!")

    