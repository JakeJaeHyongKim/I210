class puppy(object):
    
    def __init__(self, name):
        
        self.name=name
        self.barks=0
        
    def number(self):
        self.barks+=1
        print("Bark!")
        print(self.name,"has barked", self.barks, "time(s).")
        


#main
puppy1=puppy("Spot")
for i in range(5):
    (puppy1.number())
    
