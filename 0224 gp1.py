#Set blank lists
odds=[]
evens=[]
others=[]

#Numbers from the user, and sort into the lists
for i in range(10):
    user_in=eval(input("Please enter a number:"))

    if user_in%2==0:
        evens.append(user_in)
    elif user_in%2==1:
        odds.append(user_in)
    else:
        others.append(user_in)

#print the results(main)

print("\nThe results are:")
print("Evens:", evens)
print("Odds:", odds)
print("Others:", others)
