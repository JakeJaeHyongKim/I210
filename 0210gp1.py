def dasher3(string, length=20):
    if len(string)>length:
        string="Error, string must be <20"
    dashes=(length-len(string))

    half=int(dashes/2)

    formatted="-"*half+string+"-"*half

    if (dashes%2==1):
        formatted+="-"
    return formatted
print (dasher3("Hello",10))
print (dasher3("Welcome", 15))
print (dasher3("Default", 20))
