def is_lower(string):
	for letter in string:
            if not letter.islower():
                return False
            return True
def print_lower(listOfString):
    listOfCrap=[]
    for word in listOfStrings:
        if is_lower(word):
            listOfCrap.append(word)
    return listOfCrap

print(print_lower(["Lower","haha","HAHA"])
print(is_lower("house"))
