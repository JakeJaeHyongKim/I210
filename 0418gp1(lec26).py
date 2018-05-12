from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "How do you want your burger?" ).grid()

        Label(self, text = "Cheese?").grid(row=1,column=0,sticky=W)

        self.cheese = BooleanVar()
        Checkbutton(self, text = "Yes", variable = self.cheese).grid(row=2,column=0,sticky=W)

        Label(self, text = "Select a cooking level:").grid(row=3,column=0,sticky=W)

        self.level = StringVar()
        self.level.set(value="medium")
        # The default value should be 'medium' when the program starts!
        # If you don't set a default value, ALL the options will be selected.

        Radiobutton(self,
                    text = "Rare",
                    variable = self.level,
                    value = "rare").grid(row=4,column=0,sticky=W)

        Radiobutton(self,
                    text = "Medium",
                    variable = self.level,
                    value = "medium").grid(row=5,column=0,sticky=W)

        Radiobutton(self,
                    text = "Well-done",
                    variable = self.level,
                    value = "well-done").grid(row=6,column=0,sticky=W)

        Button(self,
               text = "Place order",
               command = self.order_burger).grid(row=7,column=0,sticky=W)

        self.results_txt = Text(self, width = 70, height = 5, wrap = WORD)
        self.results_txt.grid()

    def order_burger(self):
        if self.level=="medium" and self.cheese==True:
            print("Your burger is medium and has cheese on it.")
        elif self.level=="rare" and self.cheese==True:
            print("Your burger is rare and has cheese on it.")
        elif self.level=="well-done" and self.cheese==True:
            print("Your burger is rare and has chesse on it.")
        else:
            print("Your burger is"+str(self.level)+"and does not have cheese on it.")

# main
root = Tk()
root.title("Order a Burger")
root.geometry("500x300")
app = Application(root)
root.mainloop()
 
