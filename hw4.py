#Jake Kim
#Homework 4 (03/03/2015)

#5.31

def subsetSum(numList, target):
    #for loops (for list)
    for elem_1 in numList:
        for elem_2 in numList:
            for elem_3 in numList:
                if elem_1 != elem_2 and elem_2 != elem_3 and elem_2 != elem_1:
                    if elem_1 + elem_2 + elem_3 == target:
                        #return value
                        return True
    return False

#main
print("-"*25)
print("1")
print(subsetSum([5, 4, 10, 20, 15, 19], 38))
print(subsetSum([5, 4, 10, 20, 15, 19], 10))

#5.33
def mystery(num):
    #set new var for number Array list
    numArray = [1, 1]
    #if statement
    if num <= 2:
        return num
    else:
        #for loop (range of number)
        for i in range(2, num+1):
            #append numArray to list
            numArray.append(numArray[i-1] + numArray[i-2])
    print(numArray[num])

#main
print("-"*25)
print("2")
print(mystery(0))
print(mystery(4))
print(mystery(8))
    
#5.39
def exclamation(originalString):
    #blank string
    returnString = ""
    #AEIOU setting
    vowels = ["a", "e", "i", "o", "u"]
    #for loop for every letters in string
    for letter in originalString:
        if letter in vowels:
            returnString+=letter*4
        else:
            returnString+=letter
    #return value
    returnString+="!"
    return returnString

#main
print("-"*25)
print("3")
print(exclamation("exclamation"))
print(exclamation("Indiana"))

#5.43
def evenrow(twoDlist):
    for row in twoDlist:
        #basic value of Magic var
        Magic = 0
        #for loop (for every element in magic
        for elem in row:
            Magic+=elem
        if not Magic % 2 == 0:
            #return value
            return False
    return True

#main
print("-"*25)
print("4")
print(evenrow([[1,3],[2,4],[0,6]]))
print(evenrow([[1,3,2],[3,4,7],[0,6,2]]))
print(evenrow([[1,3,2],[3,4,7],[0,5,2]]))

#5.48
def sublist(list1, list2):
    #set base value of variable
    numVar=0
    varIndex=0
    #for loop (for 2 lists)
    for elem in list2:
        if elem==list1[varIndex]:
            varIndex+=1
    if varIndex==len(list1):
        #return value
        return True
    return False

#main
print("-"*25)
print("5")
print(sublist([15,1,100],[20,15,30,50,1,100]))
print(sublist([15,50,20],[20,15,30,50,1,100]))
