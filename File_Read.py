f = open('sample.txt', 'r') #here f is the object of the opened file
# data = f.read() #read function to read content
# print(data)
# data2 =f.read(5)
# print(data2)

data = f.readline() #This will read only one line at a time.
print(data)
#Second Line
data = f.readline()
print(data)
# #Thired line
# data = f.readline()
# print(data)

f.close()