#making list for dictionary
scores={"Dan":125,"Abby":100,"Carrie":275,"Ben":150}

#print sorted order of list
print("Current players:")
print(sorted(scores.keys()),"\n")

#enter input to see scores
person=input("Please enter a player name:")

#print his/her scores
print("The score for", person, "is", scores.get(person,"0"))
