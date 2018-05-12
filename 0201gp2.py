a=input("Please enter a string in lower case:")
b=input("What letter are you looking for:")

for i in range(len(a)):
    if b==i:
        print("I found",b,"at position",i)
        
