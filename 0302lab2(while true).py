contactDict={}

while True:
    if len(contactDict)==0:
        print("No contacts in database")
    else:
        print("Contacts",sorted(contactDict.keys()))
    newOrStop=str(input("Please choose a contact, new, or stop:")).lower()

    if newOrStop=="stop":
        break
    elif newOrStop=="new":
        newName=str(input("Please enter the contact's name:"))
        newNum=str(input("Please enter their phone number:"))
        contactDict[newName.lower()]=newNum
    else:
        if not newOrStop in contactDict:
            print("That name wasn't found")
        else:
            print(newOrStop, "'s number is",newNum)
