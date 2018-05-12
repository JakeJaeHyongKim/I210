class Puppy(object):
    """A virtual puppy"""

    def __init__(self, name="Spot"):	
        self.__name = name
        self.__barkCounter = 0

    def __str__(self):
        reply = "\nPuppy object\n"
        reply += "Name: " + self.__name +"\n"
        reply += "Bark Counter: "
        reply += str(self.__barkCounter) + "\n"
        return reply
    def get_name(self):
        return self.__name
    def set_name(self):
        if set_name==(""):
            return dog1

    def bark(self):
        self.__barkCounter += 1
        print("Bark!")
        print(self.__name, "has barked", self.__barkCounter, "time(s).\n")

#main
dog1 = Puppy()

dog1.set_name("")
print(dog1.get_name())
dog1.set_name("Rex")
print(dog1.get_name())
