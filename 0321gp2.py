#functions
def funA():
    x = 10

def funB():
    global x
    x += 5

def funC():
    x = 0
    x += 10

#globals
x = 15

#main section
print("1 - The number x is", x)
funA()
print("2 - The number x is", x)
funB()
print("3 - The number x is", x)
funC()
print("4 - The number x is", x)
