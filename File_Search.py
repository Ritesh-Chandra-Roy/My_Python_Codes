# f = open('sample_write.txt', 'r')
# data = f.read().lower()
# if 'exam' in data:
#     print("Present")
# else:
#     print("not present!")

# def game():
#     return 4

# score = game()
# with open('highscore.txt', 'r') as f:
#     highscore = f.read()
# if highscore == '' or int(highscore)<score:
#     with open('highscore.txt', 'w') as f2:
#         f2.write(str(score))
# #print the line number where data is present.
# f = open('sample_write.txt', 'a')
# print("Enter the data to append in file: ")
# data2 = input()
# f.write(data2)
# f.close()
#Search via key and display the found words.
key = input("Enter the key to search: ")
key = key.lower()
with open('sample_write.txt', 'r') as f:
    line = 1
    data = f.readline().lower()
    res = []
    while  data:
        
        if key in data:
            ls2 = data.split()
            
            for word in ls2:
                if key in word:
                    res.append(word)
            
            print(f"{data}: key found at line {line} ")
        
        data = f.readline()
        line += 1
    print(f"Result from filter: {res}")
f.close()