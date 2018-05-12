def somerhing():
    python_words = {"string": "a sequence of characters",
                       "int": "a whole number (integer) "}
    while True:
        tempKey = str(input("Add something?"))

        if tempKey in python_words:
            print(python_words[tempKey])
        else:
            python_words[tempKey] = input("provide a def?")

        if eval(input("break this?")) == "Y":
            break

        print("\n",python_words)



def somethingelse():
    mainDict = {"Dan": 125, "Abby": 100, "Carrie": 275, "Ben":150}

    currentPlayers = ""

    for name in sorted(mainDict.keys()):
        currentPlayers+=name+" "

    print(currentPlayers)

    tempName = str(input("Enter player name:"))
    if tempName in mainDict:
        print("The score for",tempName,"is",mainDict[tempName])
    else:
        print("Score for",tempName," not found.")



def contactDict():
    contactDict = {}

    while True:
        if len(contactDict) == 0:
            print("No contacts in database!")
        else:
            print("Contacts:",sorted(contactDict.keys()))

        newOrStop = str(input("please choose a contact, NEW or STOP")).lower()

        if newOrStop == "stop":
            print("Stopped!")
            break
        elif newOrStop == "new":
            newContactName = str(input("Enter the contact's name:"))
            newContactPhone = str(input("Enter a phone number:"))
            contactDict[newContactName.lower()] = newContactPhone
            print("Contact Saved!")
        else:
            if not newOrStop in contactDict:
                print("That name wasn't found.")
            else:
                print(newOrStop,"'s number is",contactDict[newOrStop])

