#Jake Kim
#HW 6

#8.20

class BankAccount(object):

    def __init__(self,arg):
        #initialize the balance value
        #empty argument
        if arg == "":
            self.arg = 0
        else:
            self.arg = float(arg)

    def withdraw(self, witArg):
        # withdraws from the balance

        self.arg -= witArg
        return self.arg

    def deposit(self, addArg):
        #add deposit amount

        self.arg += addArg
        return self.arg

    def balance(self):
        #return the total balance

        return self.arg


#main
x = BankAccount(700)
print(x.balance())
x.withdraw(70)
print(x.balance())
x.deposit(7)
print(x.balance())


#8.22


class Worker(object):

    def __init__(self, name, rate):
        #initialize value
        self.name = name
        self.rate = float(rate)

    def changeRate(self, newRate):
        #change worker's pay rate
        self.rate = newRate

    def pay(self, hour):
        print("Not Implemented")

#child class      
class HourlyWorker(Worker):

    def __init__(self, name, rate):
        self.name = name
        self.rate = float(rate)

    def pay(self, hours):
        self.hours =hours

        #double pay if >40
        if hours > 40:
            amt = (40 * self.rate)+((self.hours - 40)*(2*self.hours))
            #overtime payment
        else:
            amt = self.rate * self.hours

        return amt

#child class
class SalariedWorker(Worker):

    def __init__(self, name, rate):
        self.name = name
        self.rate = float(rate)

    def pay(self, hours):
        #if nothing recorded, 40 hours
        self.hours = hours
        if hours == '':
            hours = 40

        amt = self.rate * hours

        return amt



#main
w1= Worker("Joe", 15)
w1.pay(35)

w2 = SalariedWorker('Sue', 14.50)     
print(w2.pay(60))                           

w3= HourlyWorker ("Dana", 20)
print(w3.pay(25))

w3.changeRate(35)
print(w3.pay(25))



#8.34

class Stat(object):

    lst =[]

    def __init__(self):
        self.lst =[]
        
    def add(self, number):
        self.lst.append(number)

#minimum value
    def min(self):
        return min(self.lst)

#maximum value
    def max(self):
        return max(self.lst)

    
#sum of values
    def sum(self):
        return sum(self.lst)


#number of items
    def len(self):
        return len(self.lst)

    
#average of items
    def mean(self):
        x= (sum(self.lst)/len(self.lst))
        return x

#check
    def check(self,number):
        if number in self.lst:
            return True

#main
s = Stat()
s.add(4)
s.add(8)
s.add(12)
s.add(16)

print(s.min())
print(s.max())
print(s.sum())
print(s.len())
print(s.mean())
print(s.check(12))


# 8.35
class Stack(object):

    def __init__(self):
        self.lst = []

    def push(self, pus):
        self.lst.append(pus)

    def pop(self):
        rePop = self.lst[len(self.lst) - 1]
        del self.lst[len(self.lst) - 1]
        return rePop

    def __len__(self):
        return len(self.lst)

    def __str__(self):
        return str(self.lst)

    def isEmpty(self):
        if len(self.lst) == 0:
            return True
        return False

#Main
#s = Stack()
#s.push("plate 1")
#s.push("plate 2")
#s.push("plate 3")
#print(s)
#print(len(s))
#print(s.pop())
#print(s.pop())
#print(s.pop())
#print(s)
#print(s.isEmpty())

#8.40

class BankAccount(object):

    def __init__(self, acc):
        if acc == "":
            self.acc = 0
        #<0. error
        elif acc < 0:
            self.acc = acc
            print("Illegal balance")
        else:
            self.acc = float(acc)

    def withdraw(self, withAcc):
        if self.acc < withAcc:  
            print("Overdraft")
        else:
            self.acc -= withAcc
        return self.acc

    def deposit(self, add):
        if add < 0:          
            print("Negative deposit")
        else:
            self.acc += add
        return self.acc

    def balance(self):
        return self.acc
    
#main
x = BankAccount(-10)
print(x.balance())
x.withdraw(20)
print(x.balance())
x.deposit(-8)
print(x.balance())

