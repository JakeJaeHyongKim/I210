from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="This is a a list of cities!")
        self.lbl.grid()
        self.bttn1 = Button(self, text = "1. Bloomington,IN")
        self.bttn2= Button(self, text="2. Lexington, VA")
        self.bttn3=Button(self, text="3. Typone,GA")
        self.bttn4=Button(self, text="4. San Jose, Costa Rico")
        self.bttn1.grid()
        self.bttn2.grid()
        self.bttn3.grid()
        self.bttn4.grid()


# main
root = Tk()
root.title("Basic Application Class GUI")
root.geometry("400x200")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
