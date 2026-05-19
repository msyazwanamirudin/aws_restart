userReply = input("Do you want to ship a package? (Enter 'yes' or 'no')")
if userReply == "yes":
    print("Great! Let me have your details.")
    name = (input("\nName please:"))
    weight = (input("\nCan we have the estimated weight of the package?"))
    location = (input("\nPlease enter the destination location:"))
    number = (input("\n Can we have your contact number?"))
    dictionary = {"Name": name , "Weight": weight , "Location" : location , "Contact Number": number}
    print ("\nThank you for the information Mr/Ms. " + name + ". We will ship your package to " + location + " as soon as possible. We will infrom you about the delivery through your contact number " + number + ".")
else:
    print("\nNo worries. Let us know if you change your mind.Thank you for visiting our website.")