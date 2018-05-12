from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="Enter product information")
        self.lbl.grid()
        
        self.pw_lbl=Label(self,text="Product name:")
        self.pw_lbl.grid(row=1, column=0,sticky=W)
        self.pw_ent = Entry(self, width=50)
        self.pw_ent.grid(row=1, column=1, sticky=W)
        
        self.pw_lbl1=Label(self,text="Price:")
        self.pw_lbl1.grid(row=2, column=0,sticky=W)
        self.pw_ent1 = Entry(self,width=50)
        self.pw_ent1.grid(row=2, column=1,sticky=W)

        self.pw_lbl1=Label(self,text="Category:")
        self.pw_lbl1.grid(row=3, column=0,sticky=W)
        self.pw_ent1 = Entry(self,width=50)
        self.pw_ent1.grid(row=3, column=1,sticky=W)

        self.pw_lbl1=Label(self,text="UPC code:")
        self.pw_lbl1.grid(row=4, column=0,sticky=W)
        self.pw_ent1 = Entry(self,width=50)
        self.pw_ent1.grid(row=4, column=1,sticky=W)

        self.pw_lbl2=Label(self,text="Description:")
        self.pw_lbl2.grid(row=5, column=0,sticky=W)
        self.txt=Text(self,width=60,height=3,wrap=WORD)
        self.txt.grid(row=6,column=0,sticky=W)
        
        self.bttn1 = Button(self, text = "save")
        self.bttn1.grid(row=7,column=0,sticky=E)
        self.bttn2=Button(self, text="clear")
        self.bttn2.grid(row=7, column=1,sticky=W)


# main
root = Tk()
root.title("Basic Application Class GUI")
root.geometry("500x450")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
