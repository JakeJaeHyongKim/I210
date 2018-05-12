# Group HW 2

# 8.25
class Textfile(object):

    def __init__(self, fileName):
        self.file = open(fileName, 'r+')
        self.everyStr = self.file.read()

    def __str__(self):
        return "none"

    def nchars(self):
        count = 0
        for char in self.everyStr:
            count += 1
        return count

    def nwords(self):
        return len(self.everyStr.split())

    def nlines(self):
        return len(self.everyStr.split("\n"))

    def read(self):
        return self.everyStr

    def readlines(self):
        return self.everyStr.split("\n")

    def grep(self, searchKey):
        start=0
        returnStr=""
        for line in  self.everyStr.split("\n"):
            if searchKey in line:
                returnStr+=str(start)+": "+str(line)+"\n"
            start+=1
        return returnStr
    

    # 8.26
    def words(self):
        lst = []
        for word in self.everyStr.split():
            if word not in lst:
                lst.append(word)
        return lst

    # 8.27
    def occurrences(self):
        dic = {}
        for word in self.everyStr.split():
            if word in dic:
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1
        return dic
    

    # 8.28
    def average(self):
        max = 0
        min = 0
        total = 0
        count = 0
        for sentance in self.everyStr.replace("!",".").replace("?",".").split("."):
            if len(sentance) != 0:
                countr += 1
                total += len(sentance)
                if len(sentance) > max:
                    max = len(sentance)
                if min == 0:
                    min = len(sentance)
                else:
                    if len(sentance) < min:
                        min = len(sentance)
        return ((total / count), max, min)

# main
# newTextFile = Textfile("texas.txt")
# print(newTextFile.nchars())
# print(newTextFile.nwords())
# print(newTextFile.nlines())
# print(newTextFile.read())
# print(newTextFile.readlines())
# print(newTextFile.grep("Cthulu"))
# print(newTextFile.words())
# print(newTextFile.occurrences())
# print(newTextFile.average())

# 8.35
class Stack(object):

    def __init__(self):
        self.list = []

    def push(self, pus):
        self.list.append(pus)

    def pop(self):
        repop = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]
        return repop

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False

# Main
# s = Stack()
# s.push("plate 1")
# s.push("plate 2")
# s.push("plate 3")
# print(s)
# print(len(s))
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s)
# print(s.isEmpty())


# --------------------------------------------


# 8.36
class PriorityQueue(object):

    def __init__(self):
        self.prioList = []

    def __len__(self):
        return len(self.prioList)

    def __str__(self):
        return str(self.prioList)

    def insert(self, num):
        self.prioList.append(num)

    def min(self):
        return min(self.prioList)

    def removeMin(self):
        self.prioList.remove(min(self.prioList))

    def isEmpty(self):
        if len(self.prioList) == 0:
            return True
        return False

#main
# pq = PriorityQueue()
# pq.insert(3)
# pq.insert(8000)
# pq.insert(100000)
# print(pq.min())
# print(pq)
# pq.removeMin()
# print(pq)
# print(pq.isEmpty())
