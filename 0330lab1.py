class Robot(object):
    """A virtual race car"""

    def __init__(self, robotName, weapon, strength, status=True):
        self.name = robotName
        self.weapon = weapon
        self.strength = strength
        self.status = status

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


# main
r2d2 = Robot("R2D2", "Beeps", 2)
c3p0 = Robot("C3P0", "Conversation", 2, False)

print(r2d2)
print(c3p0)
