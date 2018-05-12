class Property(object):
    
    property_list = []
    
    def __init__(self, address, purchase_price):
        self.address = address
        self.purchase_price = float(purchase_price)
        self.current_value = float(purchase_price)
        self.occupied = False
        Property.property_list.append(self)

    def __str__(self):
        reply = "Property: " + self.address + "\n"
        reply += " Purchase Price: $" + str(self.purchase_price) + "\n"
        reply += " Current Value: $" + str(self.current_value) + "\n"
        reply += " Occupied: " + str(self.occupied) + "\n"
        return reply

    def __cmp__(self, other):
        if self.current_value > other.current_value:
            return 1
        elif self.current_value == other.current_value:
            return 0
        elif self.current_value < other.current_value:
            return -1

# Function which swaps the status of self.occupied
    def swap(self):
        print ("Swapping " + self.address + "'s Occupied Status.\n")
        if self.occupied == True:
            self.occupied = False
        else:
            self.occupied = True

# Function which prints out all Properties in the property_list
    @staticmethod
    def print_all():
        print ("Current Properties are:")
        for property in Property.property_list:
            print (property)

# Function which prints out the Property with the largest current_value
    @staticmethod
    def most_expensive():
        print ("The Most Expensive Property is:")
        more_expensive = 0
        for property in Property.property_list:
            if property.current_value > more_expensive:
                more_expensive = property.current_value
        for property in Property.property_list:
            if property.current_value == more_expensive:
                print (property)
                break

# Function which prints out all Properties that have increased in value
    @staticmethod
    def good_investments():
        print ("The Properties that are worth more now are:")
        for property in Property.property_list:
            if property.current_value > property.purchase_price:
                print (property)

# A new class CommercialProperty which is the child class of Property
class CommercialProperty(Property):

    def __init__(self, address, purchase_price, interest_rate):
        self.address = address
        self.purchase_price = float(purchase_price)
        self.current_value = float(purchase_price)
        self.occupied = False
        self.interest_rate = interest_rate

    def __str__(self):
        reply = "Commerical Property: " + self.address + "\n"
        reply += " Purchase Price: $" + str(self.purchase_price) + "\n"
        reply += " Current Value: $" + str(self.current_value) + "\n"
        reply += " Occupied: " + str(self.occupied) + "\n"
        reply += " Interest Rate: " + str(self.interest_rate) + "%" + "\n"
        return reply

#Function which calculates the current value based on the interest rate
    def annual_update(self):
        if self.current_value > 200000:
            self.current_value += (self.current_value * self.interest_rate/100.0)
            self.current_value = round(self.current_value, 2)
        elif self.current_value < 200000:
            self.current_value -= 10000            

# Test Code for Part 3
store = CommercialProperty("4362 Main Street", 197502.45, 3)

print ("-" * 60)

print (store)

print ("This Property loses value the first year:")
store.annual_update()
print (store)

store.swap()

print ("The value then increases by $20000:")
store.current_value += 20000
print (store)

print ("After 10 years:")

for i in range(10):
    store.annual_update()

print (store)
