import  tools

def loadingTheData(fileName):
    theFile = open(fileName+".txt", 'r')
    content = theFile.readlines()

    # stores all the dict stuff
    returnDict = {}

    # Tracks the total for percentage BONUS
    totaltrackr = 0

    for elem in content:
        tempSplit = elem.strip().split("\t")

        # If already doesn't exist, then make a place in dictonary for it.
        if not tempSplit[0] in returnDict:
            returnDict[tempSplit[0]] = int(tempSplit[1])
            totaltrackr+=int(tempSplit[1])
        else:
            returnDict[tempSplit[0]] = int(returnDict[tempSplit[0]]) + int(tempSplit[1])
            totaltrackr+=int(tempSplit[1])

    # Will store the sorted array
    sortedArray = []

    # Stores things already added to the sorted Array for increase efficiency
    tempComplete = []

    # Tracks percentages to print later
    percentTrackr = []

    # Two loops: one to cound and other to compare
    for elem, key in returnDict.items():

        # Reset every time before looping to find max
        largestElem = [0,0]
        for elem_2, key_2 in returnDict.items():

            # if it is larger than current max and not already added into master array
            if key_2 > largestElem[1] and not elem_2 in tempComplete:
                largestElem = [elem_2, key_2]

        tempComplete.append(largestElem[0])

        # Some magic to make percentages look nice
        percentTrackr.append([largestElem[0], str(round((largestElem[1] / totaltrackr) * 100,2))+"%"])

        sortedArray.append(largestElem)

    print("The candidate earned this many votes:")
    tools.table_print(["Name","Votes"],sortedArray,15)

    print("The breakdown by percent:")
    tools.table_print(["Name","Percentage"],percentTrackr,15)


# Main

# Kept loop out because no reason to be in a function..
while True:
    inputVar = str(input("Which state's totals would you like to compute? (or STOP)"))
    if inputVar.lower() == "stop":
        break
    else:
        loadingTheData(inputVar)
