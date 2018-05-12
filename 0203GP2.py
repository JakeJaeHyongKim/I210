#function definition
def dasher2(string):
    if len(string) > 20:
        string="ERROR"
    remaining=20-len(string)
    if remaining%2==0:
        even=int(remaining/2)
        return "-"*even + string + "-"*even

        
    elif string<20 and string%2==0:
        return ("-"*int((string.length)/2) +string+"-"*int(string.length/2))
        
    elif string.length<20 and not string.length%2==0:
        return ("-"*int(((string.length)/2)-1) +string+"-"*int((string.length/2)+1))
    
                      
#main section of the program
#print(dasher2("Hello"))
#print(dasher2("Welcome"))
#print(dasher2("Presentation is fun"))
