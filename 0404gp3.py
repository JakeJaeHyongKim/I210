class Car(object):
    """A virtual car"""
    
    def __init__(self, make="BMW"):
        #constructor
        self.miles = 0
        self.make = make

    def __str__(self):
        reply = "Car object\n"
        reply += "Make: " + self.make + "\n"
        reply += "Mileage: " + str(self.miles) + "\n"
        return reply

    def info(self):
        print("This car is a", self.make + ".")
        print("It has", self.miles, "miles on it.")

class Van(Car):
    def __init__(self, make, seating):
        #this calls the parent's (Car's) __init__ method first, which
        #sets up miles and make. You don't need to change this.
        reply = "Car object\n"
        reply += "Make: " + self.make + "\n"
        reply += "Mileage: " + str(self.miles) + "\n"
        
        super().__init__(make)
        self.seating=seating
        #a van also needs attributes for the number of seats in the van
        #and the current number of passengers

    def __str__(self):
        reply = "Van object\n"
        #fill in the rest of the to string method
        super().__str__()
        
        #to show ALL the attributes of the van
        #including those that come from the parent
        return reply

    def pick_up(self, num):
        #a van can only pick up passengers if it has enough
        #room for them (if there's enough seating left given
        #the current number of passengers)
        while num<=self.seating:
            print(str(num),"passengers picked up")

        #the word pass is here to make this otherwise empty
        #method not cause an error. You can remove it when
        #you start adding real code here.
        pass

#main (don't change this!)
transport = Van("Ford", 16)
print(transport)

for i in range(5):
    transport.pick_up(4)

print(transport)
