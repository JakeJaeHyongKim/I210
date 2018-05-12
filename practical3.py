#Practical 3
import random
class Investment(object):
    investments = []

    def __init__(self, name, initial_balance):
        self.name = name
        self.current_balance = float(initial_balance)
        self.initial_balance = float(initial_balance)
        Investment.investments.append(self)
        

    def __str__(self):
        reply = "Investment: " + str(self.name)
        reply += "\n Initial Balance: " + "$" + str(self.initial_balance)
        reply += "\n Current Balance: " + "$" + str(self.current_balance)
        reply += "\n Interest Rate: " + str(self.interest_rate) + "%\n"
        return reply

    def __cmp__(self, other):
        if self.current_balance > other.current_balance:
            return True
        elif self.current_balance < other.current_balance:
            return False
        else:
            return False
        

    def swap(self, other):
        print ("\nSwapping " + self.name + " and " + other.name + ".")
        self.current_balance, other.current_balance = other.current_balance, self.current_balance
        
        
    @staticmethod
    def print_all():
        for investment in Investment.investments:
            print ("Current Investments are:")
            print (gold)
            print()
            print (pork)
            print()
            print (apple)
            break

    @staticmethod
    def print_losers():
        print ("\nThe Losing Investments are:")
        for investment in Investment.investments:
            if investment.current_balance < investment.initial_balance:
                print (investment)
            

    @staticmethod
    def smallest():
        print ("The Smallest investment is:")
        smallest = 0
        for investment in Investment.investments:
            if investment.current_balance < smallest:
                smallest = investment.current_balance               
        for investment in Investment.investments:
            if investment.current_balance == smallest:
                print (investment)
                break

class SavingsAccount(Investment):

    def __init__(self, name, initial_balance, interest_rate):
        self.name = name
        self.__current_balance = float(initial_balance)
        self.initial_balance = float(initial_balance)
        self.interest_rate = interest_rate
        
        

    def annual_update(self):
        print ("SavingsAccounts Investment: " + self.name)
        if self.__current_balance < 1000:
            self.__current_balance - 10
        elif self.__current_balance >= 1000:
            self.__current_balance * 1.04

    @property
    def current_balance(self):
        return self.__current_balance

    @current_balance.setter
    def current_balance(self, new):
        if new == "":
            print ("No single transaction may empty an investment!\n")
        else:
            self.__current_balance = new
            print ("Transaction allowed.\n")
        
        
        


#test code
account1 = SavingsAccount("IUCU", 900.05, 4)

print ("-" * 60)

print (account1)

account1.current_balance += 200.56
print (account1)

account1.current_balance -= account1.current_balance
print (account1)

print(Investment.print_all)
