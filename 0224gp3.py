sum=0
num=input("Please enter a number or stop:")

while num.upper()!="stop":
    sum+=int(num)
    num=input("Please enter a number or stop:")

print("The total sum is", sum)
