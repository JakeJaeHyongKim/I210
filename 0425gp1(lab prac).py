from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Design Your Movie:").grid(row = 0, column = 2)
        Label(self, text = "Name:").grid(row = 1, column = 0, sticky = W)
        Label(self, text = "Genre:").grid(row = 2, column = 0, sticky=W)
        Label(self, text = "Rating:").grid(row = 3, column = 0, sticky=W)
        Label(self, text = "Budget: $").grid(row = 4, column = 1, sticky=E)       
        Label(self, text = "Actors:").grid(row = 5, column = 0, sticky=W)     

        self.movie = StringVar()
        self.movie.set("Action")
        Radiobutton(self, text="Action", value="Action", variable=self.movie).grid(row=2, column=1, sticky=W)
        Radiobutton(self, text="Comedy", value="Comedy", variable=self.movie).grid(row=2, column=2, sticky=W)
        Radiobutton(self, text="Documentary", value="Documentary", variable=self.movie).grid(row=2, column=3, sticky=W)
        Radiobutton(self, text="Drama", value="Drama", variable=self.movie).grid(row=2, column=4, sticky=W)
        
        self.rate = StringVar()
        self.rate.set("G")
        Radiobutton(self, text="G", value="G", variable=self.rate).grid(row=3, column=1, sticky=W)
        Radiobutton(self, text="PG", value="PG", variable=self.rate).grid(row=3, column=2, sticky=W)
        Radiobutton(self, text="PG-13", value="PG-13", variable=self.rate).grid(row=3, column=3, sticky=W)
        Radiobutton(self, text="R", value="R", variable=self.rate).grid(row=3, column=4, sticky=W)
        
        self.name = Entry(self, width=90)
        self.name.grid(row=1, column=1, columnspan=6, sticky=W)

        self.budget = Entry(self, width=40)
        self.budget.grid(row=4, column=2, columnspan=3,sticky=W)
        
        self.robert = BooleanVar()
        Checkbutton(self, text = "Robert Downey Jr.", variable = self.robert).grid(row = 5, column = 1, sticky = W)
        self.chris = BooleanVar()
        Checkbutton(self, text = "Chris Hemsworth", variable = self.chris).grid(row = 5, column = 2, sticky = W)
        self.dwayne = BooleanVar()
        Checkbutton(self, text = "Dwayne Johnson", variable = self.dwayne).grid(row = 5, column = 3, sticky = W)
        self.angelina = BooleanVar()
        Checkbutton(self, text = "Algelina Jolie", variable = self.angelina).grid(row = 6, column = 1, sticky = W)
        self.mila = BooleanVar()
        Checkbutton(self, text = "Mila Kunis", variable = self.mila).grid(row = 6, column = 2, sticky = W)
        self.julia = BooleanVar()
        Checkbutton(self, text = "Julia Roberts", variable = self.julia).grid(row = 6, column = 3, sticky = W)
        
        self.chairs = PhotoImage(file="chair.gif")
        Button(self, image = self.chairs, command=self.chair).grid(row = 5, column = 4, rowspan=3, sticky=E)

        self.results = Text(self, width=75, height=3, wrap = WORD)
        self.results.grid(row = 8, column = 0, columnspan = 6)

    def chair(self):
        print('ffd')
        print(self.movie.get())
        
        message = self.name.get() + " an ingenious "+self.movie.get()+" rated "+self.rate.get()+" $ "+str(self.budget.get())+", "
        message+= ", stars "
        actors = []
        percentage=100
        
        if self.robert.get():
            actors.append("Robert Downey Jr.")

        if self.chris.get():
            actors.append("Chris Hemsworth")

        if self.dwayne.get():
            actors.append("Dwayne Johnson")

        if self.angelina.get():
            actors.append("Angelina Jolie")
            
        if self.mila.get():
            actors.append("Mila Kunis")

        if self.julia.get():
            actors.append("Julia Roberts")

        actors = ", ".join(actors)

        if not actors:
            actors = "no one you've heard of"

        message += actors + "."

        result = random.randrange(100) + 1

        if result > int(self.budget.get()) / 1000:
            message += "\nIt got approved!"
        else:
            message += "\nThe studio passed on this one..."

        self.results.delete(0.0, END)
        self.results.insert(0.0, message)


# main
root = Tk()
root.title("Pitch a movie")
root.geometry("600x450")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
