from tools import *

class Puppy(object):
    
    puppy={}
    
    def __int__(self,name="Spot"):
        self.name=name
        self.barkCounter=0
        if name in Puppy.puppy:
            Puppy.puppy[name]+=1
        else:
            Puppy.puppy[name]=1
            
    @staticmethod
    
    def dog_name():
        tools.table_print(["Name","Times"],Puppy.puppy.item(),10)
 

    def number(self):
        print("Bark!")
        print(self.name,"has barked",self.barkCounter,"time(s):\n")
        
#main
dog1=Puppy("Spot")
dog2=Puppy("Spot")
dog3=Puppy("Rower")
dog4=Puppy("Rower")
dog5=Puppy("Rower")
dog6=Puppy("Lattle")
