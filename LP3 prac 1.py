class Fish(object):

    def __init__(self, name, length):
        self.name=name
        self.length=length
        self.caught=False

        print("Fish get in pond:"+self.name)

    def __str__(self):
        reply="Name:"+self.name+"\n"
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
        
                
                
        
#test code for v1
fish1 = Fish("Bass", 10)
fish2 = Fish("Goldfish", 2)
fish3 = Fish("Shark", 50)

# comment parts of this test code in as you implement them above
print(fish1)
print(fish2)
print(fish3)

print(fish1.name, "is longer than", fish2.name, ":", fish1 > fish2)
print(fish1.name, "is longer than", fish3.name, ":", fish1 > fish3)
print()

fish1.catch()
fish1.catch()
