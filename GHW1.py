#4.29
def stats(file):
    thisFile = open(file, 'r')
    content = thisFile.readlines()

    lineCounter = 0
    wordCounter = 0
    charCounter = 0

    for line in content:
        #total
        lineCounter+=1

        #Count chars on "line"
        for char in line:
            charCounter+=1

        #split words
        for word in line.split(" "):
            #take out hiding spaces
            if not word.isspace():
                wordCounter+=1

    print("line count:",lineCounter)
    print("word count:",wordCounter)
    print("charecter count:",charCounter)

    # Close
    thisFile.close()



#4.30
def distribution(file):
    thisFile = open(file, 'r')
    content = thisFile.read()
    content = content.split(" ")

    #list of grades
    potentialGradesList = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']

    # For loop to count each grade
    for potentialGrade in potentialGradesList:

        #no list, if there is none
        if content.count(potentialGrade) != 0:
            print(content.count(potentialGrade),"students got",potentialGrade)
    thisFile.close()

#4.31    
def duplicate(theFileName):
    thisFile = open(theFileName, 'r')
    content = thisFile.readlines()

    #blank list
    masterList = []

    #add line to list
    for line in content:
        masterList+=line.split(" ")

    #check
    for word in masterList:
        if masterList.count(word) > 1 and word.isalpha():
            return True
    return False
    thisFile.close()



# Main

stats('example.txt')

distribution('grades.txt')

print(duplicate('Duplicates.txt'))

print(duplicate('NoDuplicates.txt'))


#Chess game

#step 1. file select
def chessGame():
    thisFile=open(str(input("please enter a name of file:")), "r")
    content=thisFile.read()
    content=content.split("\n")

    #step2 displayu file formatted

    stringFormat="{counter},white moves {piece} to {move}   Black moves {piece2} to {move2}"
    print("Game moves so far:")
    counter=1

    for moveSet in content:
        print(stringFormat.format(counter=counter, piece=moveSet.split(" ")[0][0], move=moveSet.split(" ")[0][1:], piece2=moveSet.split(" ")[1][0], move2=moveSet.split[1][1:]))
        counter+=1
    
    #step 3, keep track of move
    
    while True:
        player1_move=str(input("Please enter player1's move:"))
        player2_move=str(input("Please enter player2's move:"))

        content.append(player1_move+" "+player2_move)

        if str(input("would you like to enter another move? Y/N"))=="N":
            break

    #step 4. no more turn, write out the entire game
    save_data=""
    for i in range(len(content)):
        if i<len(content)-1:
            save_data+=content[i]+"\n"
        else:
            save_data+=content[i]

    #replace contents
    thisFile.seek(0)
    thisFile.write(save_data)

    #replace entire doc
    thisFile.truncate()

    print("Thank you, your game has been saved.")
    thisFile.close()

#main
chessGame()
