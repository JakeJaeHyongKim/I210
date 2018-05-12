#Jake Kim
#HW 7

#question from the book
from tkinter import *
#random to use random choice
import random
#basic form
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.element=random.randrange(10)
        self.create_widgets()

    def create_widgets(self):      
        
        #label for entering guess
        self.guess_lbl=Label(self, text="Enter your Guess.")
        self.guess_lbl.grid()
        
        #entry field to accept
        self.name_ent=Entry(self)
        self.name_ent.grid()
        

        #submit button
        self.submit_bttn=Button(self, text="Enter", command=self.reveal)
        self.submit_bttn.grid(row=5, column=0, sticky=W)
        #bind guess2
        self.name_ent.bind('<Return>', self.guess2)
        
    def reveal(self):
        new_root=Tk()
        if self.name_ent.get()==str(self.element):
            #random choice of number
            self.element=random.choice(range(10))
            new_lbl=Label(new_root, text = "Let's do this again...", width=30, height=5)
            new_lbl.grid()
    
        else:
            #if the number is incorrect
            new_lbl=Label(new_root, text = "Incorrect", width=30, height=5)
            new_lbl.grid()

#take one argument for above
    def guess2(self, reveal):
        self.reveal()

# main
root=Tk()
root.title("Guessing Game")
root.geometry("300x200")

app=Application(root)

root.mainloop()



#additional question

from tkinter import *
#basic format
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    #creat widgets in form 
    def create_widgets(self):
        self.deliver_lbl=Label(self, text="What would you like delivered?")
        self.deliver_lbl.grid(row=0,column=0,sticky=W)

        self.ent_lbl=Entry(self)
        self.ent_lbl.grid(row=0,column=1,sticky=W)

        self.option_lbl=Label(self,text="Options:")
        self.option_lbl.grid(row=1,column=1,columnspan=3,sticky=W)

        #label for each side of button
        Label(self, text = "Delivery Method:").grid(row = 2, column = 0)
        #StringVar to use radio buttons
        self.method = StringVar()
        self.method.set(None)
        #Delivery methods using radio buttons
        Radiobutton(self, text = "Flying Drone ($10)", variable = self.method, value = "$10").grid(row = 3, column = 0, sticky = S)

        Radiobutton(self, text = "Self Driving Car ($20)", variable = self.method,  value = "$20").grid(row = 4, column = 0, sticky = S)

        Radiobutton(self, text = "Giant Robot ($1000)", variable = self.method,  value = "$1000").grid(row = 5, column = 0, sticky = S)

        Label(self,text="Addons:").grid(row=2,column=2)
        #add on check buttons
        self.express_delivery = BooleanVar()
        Checkbutton(self,
                    text= "Express Delivery ($30)",
                    variable= self.express_delivery,
                    command = self.price
                    ).grid(row = 3, column = 2, sticky = S)

        # create Mostly Not Broken check button
        self.mostly_not_broken = BooleanVar()
        Checkbutton(self,
                    text="Mostly Not Broken($20)",
                    variable = self.mostly_not_broken,
                    command = self.price
                    ).grid(row = 4, column = 2, sticky = S)

        # create With a Smile check button
        self.with_smile = BooleanVar()
        Checkbutton(self,
                    text = "With a Smile($1)",
                    variable = self.with_smile,
                    command = self.price
                    ).grid(row = 5, column = 2, sticky = S)
        #confirm button
        Button(self, text = "Confirm Delivery", command = self.price).grid(row=6, column = 1, sticky = W)

        # create text field to display total price and result
        self.results_txt = Text(self, width = 70, height = 5, wrap = WORD)
        self.results_txt.grid(row = 7, column = 0, columnspan = 3)
    #funtion does not work...but I think this is how I should approach to
    def price(self):
        message="You have selected to have a"+str(self.ent_lbl.get())+"delivered by"+str(self.method.get())+"with"
        #count total price
        price=0
        #additional message depends on radio button
        for check in self.method:
            if self.method.get(value)=="$10":
                price+=int(self.method.get(value))
                message+=": "+price
            elif self.method.get(value)=="$20":
                price+=int(self.method.get(value))
                message+=": "+price
            elif self.method.get(value)=="$1000":
                price+=int(self.method.get(value))
                message+=": "+price
                
        #additional message depends on check button     
        if self.express_delivery.get():
            message+="express delivery: "+price
            price+=int(self)

        if self.mostly_not_broken.get():
            message+="mostly not broken: "+price
            price+=self

        if self.with_smile.get():
            message+="with a smile: "
            price+=self

        self.price.delete(0.0, END)
        self.price.insert(0.0, likes)
        
#main for application
root = Tk()
root.title("Robot Delivery System")
root.geometry("600x450")

app = Application(root)

root.mainloop()
