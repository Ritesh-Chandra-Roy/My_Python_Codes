info = {"Name": "Ritesh", "Vehical": "Car", "Salary" : 10000, "Skills" : ["Django", "OpenCV", "MongoDB"]}
# print(info["Name"])
# print(info["Skills"])
# print(info["Salary"])
# Dictionary inside Dictionary
myDict ={
    "Gujarat" : "Rajkot", 
    "States" : {"Bihar" : "Patna", "karnataka" : "Bangaloru", "Maharastra" : "Mumbai"}
}
# print(myDict["States"]["Bihar"])
myDict['Gujarat'] = 'Ahmedabad' #latest value will replace the old if key already exists!!
# print(myDict['Gujarat'])
# Methods
# print(info.keys()) 
# print(info.values())
print(myDict.items())
info.update(myDict)
print(info)
print(myDict.get("Punjab")) #Will throw null if key not present // use this in programs to fetch values