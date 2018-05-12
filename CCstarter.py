from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.num_clicks=0
        self.create_widgets()

    def create_widgets(self):
        self.lbl=Label(self, text="Click to increment")
        self.lbl.grid()
        self.bttn = Button(self, text="Total clicks: 0", command=self.new_click)
        self.bttn["text"]= "Total clicks:"
        self.bttn.grid()

    def update_button(self):
        self.num_clicks+=1
        self.bttn1["text"]="Total clicks:"+str(self.num_clicks)
    

# main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()


