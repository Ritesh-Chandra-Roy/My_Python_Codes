n = 5
for i in range(n):
    print(" " * (n-i-1), end="") #end = "" is used to avoid the new line character
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
    
