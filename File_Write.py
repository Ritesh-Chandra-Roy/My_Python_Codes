f = open('sample_write.txt', 'w') #this will overwrite the content of file
f.write("I am writing in this file")
f.close()
#Append
f2 = open('sample_write.txt', 'a') #this will append the the existing data
f2.write("This line was appended!")
f2.close()