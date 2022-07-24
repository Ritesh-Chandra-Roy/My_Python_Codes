str = "}}"
stack = []
for char in str:
    if char == '(' or char == '{' or char == '[':
        stack.append(char)
    elif  char == ')' or char == '}' or char == ']':
        if not stack:
            print("Not valid String case : 1")
            break
        if  (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[') or (char == '}' and stack[-1] == '{'):
            stack.pop()
        else:
            stack.append(char)
            print(stack)
            print("Not a valid string case : 2")
            break
    if stack:
        print(stack)
else:
    if not stack:
        print("Valid String!!")
    else:
        print("Invalid String case : 3")