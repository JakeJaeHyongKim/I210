message=input("Please enter a messages:")
newmessage=message.split(" ")
print("That message had",len(newmessage), "words")
longest=newmessage[0]

for i in newmessage:
    if len(i)>len(longest):
        longest=i

print("The longest word was:", longest)
