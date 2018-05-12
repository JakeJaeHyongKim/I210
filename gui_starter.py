from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="Enter student information")
        self.lbl.grid()
        self.pw_lbl=Label(self,text="student name:")
        self.pw_lbl.grid(row=1, column=0,sticky=W)
        
        self.pw_ent = Entry(self, width=50)
        self.pw_ent.grid(row=1, column=0, sticky=E)
        self.pw_lbl1=Label(self,text="GPA:")
        self.pw_lbl1.grid(row=2, column=0,sticky=W)
        self.pw_ent1 = Entry(self,width=50)
        self.pw_ent1.grid(row=2, column=0,sticky=E)

        self.pw_lbl2=Label(self,text="Essay:")
        self.pw_lbl2.grid(row=3, column=0,sticky=W)
        self.txt=Text(self,width=60,height=8,wrap=WORD)
        self.txt.grid(row=4,column=0,sticky=W)
        
        self.bttn1 = Button(self, text = "save")
        self.bttn1.grid(row=5,column=0,sticky=W)
        self.bttn2=Button(self, text="clear")
        self.bttn2.grid(row=5, column=0,sticky=E)


# main
root = Tk()
root.title("Basic Application Class GUI")
root.geometry("430x250")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
