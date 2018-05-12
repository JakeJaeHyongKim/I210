number=eval(input("please enter a number:"))
remainder=number%2
if remainder in (0,1):
    if remainder==0:
        print("Even number detected")
    else:
        print("odd number!")
else:
    print("Brace yourself - that's not a whole number!")
