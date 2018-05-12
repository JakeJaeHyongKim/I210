import random


class Robot(object):
    """A virtual race car"""
    robot_list=[]

    def __init__(self, robotName, weapon, strength, status=True):
        self.name = robotName
        self.weapon = weapon
        self.strength = strength
        self.status = status
        new_robot=list((self.name,self.weapon,self.strength,self.status))
        Robot.robot_list.append(self)

        print("Robot created! " + self.name)

    def __str__(self):
        reply = "--------------------" + "\n"
        reply += "Fighting Robot" + "\n"
        reply += "Name:" + self.name + "\n"
        reply += "Weapon:" + self.weapon + "\n"
        reply += "Strength:" + str(self.strength) + "\n"

        if self.status:
            reply += "Status: ONLINE" + "\n"
        else:
            reply += "Status: OFFLINE" + "\n"

        reply += "--------------------"
        return reply
    
    def contenders():

        print("There are",len(Robot.robot_list),"robots.")

        for robot in Robot.robot_list:
            print(robot)
            
    def fight(self, other):
        print(self.name+" challenges "+other.name)
        print("Closse match!!!")
        if self.status==False:
            print(self.name+" cannot fight-it is offline")
        elif other.status==False:
            print(other.name+" cannot fight-it is offline")
        else:
                if self.strength>other.strength:
                    print(self.name+" wins, using its "+self.weapon)
                    other.status=False
                elif self.strength==other.strength:
                    winner=random.choice([self, other])
                    print(winner.name+" wins, using its "+winner.weapon)
                    
                else:
                    print(other.name+" wins, using its "+other.weapon)
                    self.status=False


# main
r2d2 = Robot("R2D2", "Beeps", 10)
c3p0 = Robot("C3P0", "Conversation", 10)
r2d2.fight(c3p0)
