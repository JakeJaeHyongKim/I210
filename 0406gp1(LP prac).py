# pass is used to prevent Python from throwing an error
# when a method has no code. You can remove it when you
# implement each method. There is a LOT of test code below.

class Fish(object):
    school=[]

    def __init__(self, name, length):
        self.name=name
        self.length=length
        self.caught=False
        
        Fish.school.append(self)

        print("Fish get in pond:"+self.name)

    def __str__(self):
        reply="Number of fish in the pond:"+len(school)+"\n"
        reply+="Name:"+self.name+"\n"
        reply+="Length:"+str(self.length)+"\n"

        if self.caught:
            reply+="Status: CAUGHT"+"\n"
        else:
            reply+="Status: FREE"+"\n"

        return reply

    def __gt__(self, other):
        if self.length>other.length:
            return True

        else:
            return False
            

    def catch(self):
        if self.caught:
            print("You attempt to catch Bass. Bass was already caught!")
        else:
            print("You attempt to catch. Success!")
            self.caught=True


    @staticmethod
    
    def remaining():
        print("Number of Fish in pond",len(Fish.school))

    def largest():
        length=0
        largestFish=""
        for item in Fish.school:
            if item.length>length:
                length=item.length
                largestFish=item.name
        print("The largest fish is:",largestFish,"\n")
        #print("The largest fish is:"+max(Fish.school).name)
           
###test code for v2 - delete above test code
fish1 = Fish("Bass", 10)
fish2 = Fish("Goldfish", 2)
fish3 = Fish("Shark", 50)
Fish.remaining()
Fish.largest()
fish1.catch()
Fish.remaining()

###test code for v3 - delete above test code
##fish1 = StealthFish("007", 11)
##fish2 = FancyFish("Lord","Grantham", 10)
##fish3 = NiceFish("Nemo", 3)
##fish1.catch()
##fish2.catch()
##fish3.catch()
##fish3.release()
##fish3.release()
##Fish.remaining()

