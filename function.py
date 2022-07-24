def percent(marks):
    return(sum(marks)/500) * 100

def display(percentage):
    print(f"Percentage: {percentage}")

marks1 = [40, 77, 79, 36, 84]
percentage1 = percent(marks1)
display(percentage1)

marks2 = [62, 75, 48, 57, 70]
percentage2 = percent(marks2)
display(percentage2)
#default Argument
def greet(name = 'guest'):
    print("Hello "+name)
name = "Roy"
greet(name)
greet()

def pattern(lines):
    for i in range(lines):
        print("*"*(lines-i))


lines = int(input("Enter no.of lines to print: "))
pattern(lines)