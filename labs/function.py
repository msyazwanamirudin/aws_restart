
def question():
userReply = input("Please enter yes or no: ")
    if userReply.lower() == "yes":
        print("User says yes")
    elif userReply.lower() == "no":
        print("User says no")
    else:
        print("Invalid input. Try again!")
        question() #Recursive function

question()