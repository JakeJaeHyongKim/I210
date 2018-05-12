class cellPhone(object):
    def __init__(self, owner, minutes):
        self.minutes=int(minutes)
        self.owner=owner
        
    def info(self):
        print("My owner is", self.owner+".", self.owner, "has", self.minutes, "minutes left.\n")


#main
phone1=cellPhone("Amelia",500)
phone1.info()

phone2=cellPhone("Bob", 300)
phone2.info()
