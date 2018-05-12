import random

print("Welcome to 'Guess my number'!")
#set random number
ranNum=random.randrange(1,100)
#0 count for add on
count=0

while 1<=ranNum<=100:
    num=eval(input("Take a guess:"))
    if num>ranNum:
        print("Lower!")
        count+=1
        
    elif num<ranNum:
            print("Higher!")
            count+=1
    else:
        count+=1
        print("right!",ranNum,"is guessed number",count,"tries")
        
