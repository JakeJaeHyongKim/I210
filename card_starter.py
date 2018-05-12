from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # DO NOT remove the images that come with this file from their folder!
        self.back = PhotoImage(file="cards/b.gif")      # a card back image
        self.solved = PhotoImage(file="cards/iu.gif")   # the IU logo
        self.spades = PhotoImage(file="cards/ac.gif")   # the ace of Clubs
        self.hearts = PhotoImage(file="cards/ah.gif")   # the ace of Hearts

        # You need attributes to track which card is "hidden" in each button
        # In my example, it's Clubs Hearts Hearts Clubs
        
        # You must also track whether or not a particular button has been clicked
        
        self.button0 = Button(self, image=self.back, command=self.change_image0)
        self.button0.grid(row = 0, column = 0)
        self.button1 = Button(self, image=self.back, command=self.change_image1)
        self.button1.grid(row = 0, column = 1)
        self.button2 = Button(self, image=self.back, command=self.change_image2)
        self.button2.grid(row = 0, column = 2)
        self.button3 = Button(self, image=self.back, command=self.change_image3)
        self.button3.grid(row = 0, column = 3)

        self.output = Label(self, text = "Match the Aces!")
        self.output.grid(row = 1, column = 0, columnspan = 4)

    def change_image0(self):
        # handle the first button
        pass

    def change_image1(self):
        # handle the second button
        pass

    def change_image2(self):
        # handle the third button
        pass

    def change_image3(self):
        # handle the fourth button
        pass

    def check_match(self):
        # much of what needs to be done is the same for each button
        # instead of duplicating the code, have their event handlers
        # call this method.

        # If two cards that match have been revealed, change their image
        # to the IU logo.

        # If all cards are matched, the user wins.
        pass
            
# main
root = Tk()
root.title("Card Match!")
root.geometry("320x130")
app = Application(root)
root.mainloop()
 
