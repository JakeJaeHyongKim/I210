from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.bttn_clicks=0
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="Enter two numbers")
        self.lbl.grid()
        
        self.ent=Entry(self,width=30)
        self.ent.grid()
        
        self.ent2=Entry(self,width=30)
        self.ent2.grid()
        
        self.lbl1=Label(self, text="The sum: ")
        self.lbl1.grid()

        self.bttn=Button(self, text="Add numbers",command=self.sumNum)
        self.bttn.grid()
        
    def sumNum(self):
        num1=self.ent.get()
        num2=self.ent2.get()
        total=num1+num2
        try:
            total=int(num1)+int(num2)
            self.lbl1["text"]="The sum: "+str(total)
            
        except:
            self.lbl1["text"]="Error"
        self.ent.delete(0, END)
        self.ent2.delete(0, END)

# main
root = Tk()
root.title("Basic Application Class GUI")
root.geometry("400x200")
root.resizable(width = FALSE, height = FALSE)
app=Application(root)
root.mainloop()
