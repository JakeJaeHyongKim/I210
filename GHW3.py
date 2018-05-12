#Jake Kim
#Group 40

from tkinter import *
import random

from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from calendar import monthrange

class Ed(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.setNumbers()

    def create_widgets(self):
        self.total_try = 0
        self.history = []

        self.entry1 = Entry(self, width=20)
        self.entry1.grid(row = 1, column = 1)

        self.entry2 = Entry(self, width=20)
        self.entry2.grid(row = 1, column = 2)
        self.entry2.bind('<KeyPress>', self.record)

        self.button1 = Button(self, text="Submit", command = self.calculate)
        self.button1.grid(row = 1, column=3)


    def setNum(self):
        self.entry1.delete(0, END)

        #while loop, find combos of numbers continuously
        while True:
            self.random1 = random.randrange(1,9)
            self.random_oper = random.randrange(0,2)
            self.random2 = random.randrange(1,9)

            creat_str= str(self.random1)+" - "+str(self.random2)

            if self.random_oper == 1 and creat_str not in self.history:
                if self.random1 - self.random2 >= 0:
                    break
            else:
                if self.random1 + self.random2 >= 0 and creat_str not in self.history:
                    break

        # Check the operand, and creat a string
        if self.random_oper == 1:
            creat_str1 = str(self.random1)+" - "+str(self.random2)
        else:
            creat_str1 = str(self.random1)+" + "+str(self.random2)

        if len(self.history) >= 10:
            del self.history[len(self.history) - 1]

        self.history.append(creat_str1)
        self.entry1.insert(0,creat_str1)


    # Record, if the enter button was pressed
    def record(self, event):
        if event.keysym == "Return":
            self.calculate()


    # Tracks attempts, and returns if the answer is right
    def calculate(self):

        self.total_try = int(self.total_try) + 1

        if self.random_oper == 1:
            if self.random1 - self.random2 == int(self.entry2.get()):
                showinfo("Winner!", "You got it! \nAttempts: "+str(self.total_try))
                self.total_try = 0
                self.setNum()
        else:
            if self.random1 + self.random2 == int(self.entry2.get()):
                showinfo("Winner!", "You got it! \nAttempts: "+str(self.total_try))
                self.total_try = 0
                self.setNum()

        self.entry2.delete(0, END)
        
#app creat
root = Tk()
root.title("Roman Numerals")
root.geometry("900x350")

app = Ed(root)
root.mainloop()



class Calendar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()

        self.currYear = 2012
        self.currMon = 0

        self.Calendar(2012, 2)

    # calendar, take year and month
    def Calendar(self, year, month):
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for index, day in enumerate(weekdays):
            self.title = Label(self, text=day)
            self.title.grid(row=0, column=index)

        weekday, numDays = monthrange(year, month)
        week = 1

        #list, (mostly given in book)
        for i in range(1, numDays):
            self.button1 = Button(self, text=str(i), command = self.open_dial)
            self.button1.grid(row = week, column = weekday)

            weekday += 1
            if weekday > 6:
                week+=1
                weekday=0

        #Next and Prev button (left and right bottom)
        self.button1 = Button(self, text="Next", command = self.nextMon)
        self.button1.grid(row = 7, column = 6)

        self.button1 = Button(self, text="Previous", command = self.prevMon)
        self.button1.grid(row = 7, column = 0)


    #find next month, change calendar
    def nextMon(self):
        # No 13th month, so after 12, go to new year
        if self.currMon+1 >= 12:
            self.currMon = 0
            self.currYear+=1
        else:
            self.currYear+=1
            self.currMon+=1
        self.Calendar(self.currYear+1, self.currMon+1)

    # hard one....
    def prevMon(self):
        if self.currMon-1 <= 0:
            self.currMon = 0
            self.currYear-=1
        else:
            self.currYear-=1
            self.currMon-=1
        self.Calendar(self.currYear-1, self.currMon-1)

    # Returns the result
    def open_dial(self):
        hello = askstring("example", "Enter Text")
        return hello

root = Tk()
root.title("Calendar")
root.geometry("350x200")

app = Calendar(root)
root.mainloop()
