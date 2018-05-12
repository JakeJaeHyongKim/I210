import random

class Investment:

    portfolio = []

    def __init__(self, investType, investAmount):
        self.portfolio.append(self)
        self.arrayLocation = len(self.portfolio) - 1
        self.investAmount = investAmount
        self.investType = investType
        print("Investment "+str(investType)+" created with a value of $"+str(investAmount)+"\n")

        # This re-sorts the portfolio
        Investment.portfolio = sorted(Investment.portfolio, key=lambda k: k.investAmount, reverse=True)


    def __str__(self):
        return ("Investment: "+str(self.investType)+"\nAmount: $"+str(self.investAmount)+"\n")


    def grow(self):
        print("You must define the type of investment to grow it\n")

    @staticmethod
    def show():
        returnString = "Your "+str(len(Investment.portfolio))+" investments in order of value are:\n\n"
        for investment in Investment.portfolio:
            returnString+=str(investment)+"\n"
        return returnString


class Stock(Investment):
    def grow(self):

        # Random increase based on random value
        self.investAmount = ((random.randrange(90,120) * 0.01) * self.investAmount)

        # This re-sorts the portfolio
        Investment.portfolio = sorted(Investment.portfolio, key=lambda k: k.investAmount, reverse=True)



class Bond(Investment):
    def __init__(self, investType, investAmount, investYeild):
        self.portfolio.append(self)
        self.arrayLocation = len(self.portfolio) - 1
        self.investAmount = investAmount
        self.yeilds = investYeild
        self.investType = investType
        print("Investment "+str(investType)+" created with a value of $"+str(investAmount)+"\n")

        # This re-sorts the portfolio
        Investment.portfolio = sorted(Investment.portfolio, key=lambda k: k.investAmount, reverse=True)

    def grow(self):

        # Based on yeild percentage (can't spell, really hungry!!)
        self.investAmount = (self.yeilds * self.investAmount) + self.investAmount

        # This re-sorts the portfolio
        Investment.portfolio = sorted(Investment.portfolio, key=lambda k: k.investAmount, reverse=True)




class SubprimeMortgage(Investment):
    def __init__(self, investType, investAmount):
        self.portfolio.append(self)
        self.arrayLocation = len(self.portfolio) - 1
        self.investAmount = investAmount
        self.years = 0
        self.investType = investType

        print("Investment "+str(investType)+" created with a value of $"+str(investAmount)+"\n")

        # This re-sorts the portfolio
        Investment.portfolio = sorted(Investment.portfolio, key=lambda k: k.investAmount, reverse=True)

    def grow(self):

        # Increment by 1 every year
        self.years += 1

        # If we go over 3, just reset value
        if self.years > 3:
            self.investAmount = 0
        else:
            # Good investment doubles until 3 years..?
            self.investAmount = self.investAmount * 2

        # This re-sorts the portfolio
        Investment.portfolio = sorted(Investment.portfolio, key=lambda k: k.investAmount, reverse=True)




# BONUS
def TenYearSimulation():
    changeTracker = []

    # Make a random set of 5 investments that are random with random values
    # SO MUCH RANDOM IN RANDOM IN RANDOM....
    for i in range(5):
        randomInvestment = random.randrange(0,3)
        randomeValue = random.randrange(1,100000)
        if randomInvestment == 0:
            changeTracker.append(
                {
                    "name":"Stock-"+str(i),
                    "investmentObj": Stock(str("Stock-"+str(i)), randomeValue),
                    "average":[]
                 }
            )
        elif randomInvestment == 1:
            changeTracker.append(
                {
                    "name":"Bond-"+str(i),
                    "investmentObj": Bond(str("Bond-"+str(i)), randomeValue, 0.03),
                    "average":[]
                 }
            )
        else:
            changeTracker.append(
                {
                    "name":"SubprimeMortgage-"+str(i),
                    "investmentObj": SubprimeMortgage(str("SubprimeMortgage-"+str(i)), randomeValue),
                    "average":[]
                 }
            )

    # This is where I got really confused and too hungry to continue working.. see notes where funtion is called.
    for investment in changeTracker:
        for i in range(10):
            investment["investmentObj"].grow()
            investment["average"].append(investment["investmentObj"].investAmount)

        for item in investment["average"]:
            print("Value increased by average of ")

    print(changeTracker)


# MAIN

inv0 = Investment("Test", 100)
print(inv0)
inv0.grow()
print(inv0)


inv1 = Stock("Google", 600)
inv2 = Bond("US Treasury", 600, .03)
inv3 = SubprimeMortgage("Housing", 600)
print("Starting Investments\n"+"-"*30,"\n")
print(Investment.show())

inv1 = SubprimeMortgage("Google", 600)
print("Starting Investments\n"+"-"*30,"\n")
print(Investment.show())
inv1.grow()
inv1.grow()
inv1.grow()
inv1.grow()
print(Investment.show())

inv1 = Stock("Google", 600)
inv2 = Bond("US Treasury", 1000, .03)
inv3 = SubprimeMortgage("Housing", 10000)

print("Starting Investments\n"+"-"*30,"\n")

print(Investment.show())

for investment in Investment.portfolio:
    for i in range(5):
        investment.grow()
print("Final Investments\n"+"-"*30,"\n")

print(Investment.show())
