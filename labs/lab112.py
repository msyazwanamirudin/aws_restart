#Exercise 1: Mixed type list
myMixedTypeList = [46, 123.45, "Hello.", "World.", "55"]
print (myMixedTypeList)
print (type(myMixedTypeList))

for item in myMixedTypeList:
    print(item)
    print(type(item))
    print("{} is of the data type {}".format(item,type(item)))

for i in range (2, 5):
    print(i)