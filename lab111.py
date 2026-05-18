#Exercise 1: Defining a list
myFruitList = ["apple", "orange", "grape"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[2])
print(myFruitList[1])
print(myFruitList[0])
#myFruitList[3] #This will give an error because there is no index 3
myFruitList[0] = "Durian"
print(myFruitList)


# Exercise 2: Defining a tuple
myfinalAnswerTuple = ("cherry", "mata kucing" , "strawberry")
print(myfinalAnswerTuple)
print(type(myfinalAnswerTuple))
print(myfinalAnswerTuple[0])
print(myfinalAnswerTuple[1])
print(myfinalAnswerTuple[2])


# Exercise 3: Defining a dictionary
myFavouriteFruitDictionary = {
    "red" : "apple",
    "orange" : "orange",
    "purple" : "grape"
}
print(myFavouriteFruitDictionary)
print(type(myFavouriteFruitDictionary))


# Exercise 4: Accessing dictionary by name
print(myFavouriteFruitDictionary["red"])
print(myFavouriteFruitDictionary["orange"])
print(myFavouriteFruitDictionary["purple"])
