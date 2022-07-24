# Concatinate
name = "Ritesh"
sername = "Roy"
full_name = name + sername
print(full_name)
print(name + sername)
# Slicing
print(name[0])
print(name[1])
# name[2] = "a" not possible to assign 
print(name[0:4]) #print range from index 0-3
print(name[2:5])
# print(name[:4]) same as print(name[0:4])
# print(name[1:]) same as print(name[1:len])
print(name[-1])
# skip value
sent = "Humptydumptysatonawall"
skp2 = sent[0:-1:2] #skip every 2nd value
print(skp2)
skp3 = sent[0:-1:3] #skip every 3rd value
print(skp3)
#Reverse a string using String Slicing
word1 = "Ritesh"
word2 = word1[::-1]
print(word1)
print(word2)