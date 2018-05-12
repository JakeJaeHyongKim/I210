#This program has a problem!

donuts = eval(input("Aaron, Beth, and Cody go out for donuts." + \
                    "How many donuts do they buy?: "))

while donuts :
    print("Aaron takes a donut.")
    print("Beth takes a donut.")
    print("Cody takes a donut.")
    donuts -= 3

if donuts!=0:
    print("There are", donuts,"left")
else:
    print("They took all the donuts!")
