letter = '''Dear <|NAME|>, 
You are selected!

Date: <|DATE|>
'''
print(letter)
name = input("Enter your name: ")
date = input("Enter Date: ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter) 