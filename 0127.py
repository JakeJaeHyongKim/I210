#user name
name=input("please enter your name: ")
#User age
age=eval(input("please enter your age: "))
#Welcome
print("Thanks for using this program,", name+".")
print("Nice to meet a " + str(age)+"year old!")
#Check
if age>=65:
    print("Don't forget to ask about our senior discounts!")
else:
    print("We hope you shop here until you're old!")
    
