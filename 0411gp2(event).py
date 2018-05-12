from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn = Button(self)
        self.bttn["text"]= "Light is on"
        self.bttn["command"] = self.update_button
        self.bttn.grid()
 
    def update_button(self):
        if self.bttn["text"]=="Light is off":
            self.bttn["text"]="Light is on"
        else:
            self.bttn["text"]="Light is off"

# main
root = Tk()
root.title("Event Handler Demo")
root.geometry("250x25")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
