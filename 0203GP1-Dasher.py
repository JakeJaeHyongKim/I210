#function definition
def dasher(word):
    list(word)
    return_value="-".join(word)
    
    return "-"+return_value+"-"

#main section of the program
print(dasher("Hello"))
print(dasher("Greetings"))
print(dasher(dasher("TEST?")))
