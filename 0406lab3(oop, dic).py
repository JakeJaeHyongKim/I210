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
        print(self, other)
        
    @staticmethod
    
    def weapon_check():
        dic_weapon={}
        
        for robot in Robot.robot_list:
            if robot.weapon in dic_weapon:
                dic_weapon[robot.weapon].append(robot.name)
            else:
                dic_weapon[robot.weapon]=[robot.name]
        
        for weapon in dic_weapon.keys():
            print("The robots using the "+weapon+" weapon are: ", ", ".join(dic_weapon[weapon]))

    def __lt__(self, other):
        if self.strength<other.strength:
            return True
        else:
            return False

    def random_tournament():
        sortList=sorted(Robot.robot_list)
        count=0
        finalFight=False
        
        while finalFight==False:
            count+=1
            print("Random Tournament, Round ", count)
            
            if len(sortList)==1:
                print("The ultimate winner is: "+sortList[0].name)
                finalFight=True
            
            for i in range(0,len(sortList),2):
                if i+1 >=len(sortList):
                    print(sortList[i].name+" gets a bye this round")
                else:
                    robot1=sortList[i]
                    robot2=sortList[i+1]
                    robot1.fight(robot2)
            for robot in sortList:
                if robot.status==False:
                    sortList.remove(robot)
                else:
                    return sortList
                


# main
r2d2 = Robot("R2D2", "Beeps", 10)
c3p0 = Robot("C3P0", "Conversation", 10)
bb8 = Robot("BB-8", "Beeps", 1)
j = Robot("Robot J", "Conversation", 2)
optimus = Robot("Optimus", "Fists", 10)
voltron = Robot("Voltron", "Sword", 10)
gipsy = Robot("Gipsy Danger", "Sword", 9)
Robot.random_tournament()


