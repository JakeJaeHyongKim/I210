from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Calculate Your Airfare:").grid(row = 0, column = 1)
        Label(self, text = "Customer Name:").grid(row = 1, column = 0, sticky = E)
        Label(self, text = "Select Your Options:").grid(row = 2, column = 1)
        Label(self, text = "Choose Class:").grid(row = 3, column = 0)
        Label(self, text = "Choose Airline:").grid(row = 3, column = 1)
        Label(self, text = "Inflight Extras:").grid(row = 3, column = 2)     
        Label(self, text = "Distance Traveled (miles):").grid(row = 8, column = 0)

        self.seating = StringVar()
        self.seating.set("economy")
        Radiobutton(self, text="Economy (baseline)", value="economy", variable=self.seating).grid(row=4, column=0, sticky=W)
        Radiobutton(self, text="Business (50% more)", value="business", variable=self.seating).grid(row=5, column=0, sticky=W)
        Radiobutton(self, text="Luxury (200% more)", value="luxury", variable=self.seating).grid(row=6, column=0, sticky=W)

        self.airline = StringVar()
        self.airline.set("Delta")
        Radiobutton(self, text="Delta (1 dollar per mile)", value="Delta", variable=self.airline).grid(row=4, column=1)
        Radiobutton(self, text="United (80 cents per mile)", value="United", variable=self.airline).grid(row=5, column=1)
        Radiobutton(self, text="Southwest (60 cents per mile)", value="Southwest", variable=self.airline).grid(row=6, column=1)
        Radiobutton(self, text="JetBlue (50 cents per mile)", value="JetBlue", variable=self.airline).grid(row=7, column=1)

        self.name = Entry(self, width=40)
        self.name.grid(row=1, column=1, sticky=W)

        self.distance = Entry(self, width=10)
        self.distance.grid(row=9, column=0)
        
        self.headphones = BooleanVar()
        Checkbutton(self, text = "Headphones ($4)", variable = self.headphones).grid(row = 4, column = 2, sticky = W)
        self.beverage = BooleanVar()
        Checkbutton(self, text = "Beverage ($10)", variable = self.beverage).grid(row = 5, column = 2, sticky = W)
        self.peanuts = BooleanVar()
        Checkbutton(self, text = "Peanuts ($50)", variable = self.peanuts).grid(row = 6, column = 2, sticky = W)

        self.calculator = PhotoImage(file="calculator.gif")
        Button(self, image = self.calculator, command=self.calculate).grid(row = 1, column = 2)

        self.results = Text(self, width=70, height=6, wrap = WORD)
        self.results.grid(row = 10, column = 0, columnspan = 3)

    def calculate(self):

        message = "Thanks for flying with us, " + self.name.get() + ".\n"

        message += "You've selected a " + self.seating.get() + " class flight on " + self.airline.get()+ " airlines" 

        options = []
        add_on = 0

        if self.headphones.get():
            options.append("headphones")
            add_on += 4
        if self.beverage.get():
            options.append("a beverage")
            add_on += 10
        if self.peanuts.get():
            options.append("peanuts")
            add_on += 50

        if options:
            if len(options) == 3:
                options = (", ").join(options[:-1]) + ", and " + options[-1]
            elif len(options) == 2:
                options = (", ").join(options[:-1]) + " and " + options[-1]
            else:
                options = options[0]        
            message += " with " + options + ".\n"
        else:
            message += ".\n"

        airline = self.airline.get()

        if airline == "Delta":
            price = 1
        elif airline == "United":
            price = 0.8
        elif airline == "Southwest":
            price = 0.6
        else:
            price = 0.5

        grade = self.seating.get()

        if grade == "economy":
            price *= 1
        elif grade == "business":
            price *= 1.5
        else:
            price *= 3

        withDistance = price * float(self.distance.get())

        final = round(withDistance + add_on, 2)

        message += "Your total comes to $" + str(final) + "\n"

        withTax = round(final * 1.07, 2)

        fees = int(int(self.distance.get()) / 100) * 20

        message += "With 7% tax plus $" + str(fees) + " in fees your true final cost will be $" + str(withTax + fees)

        self.results.delete(0.0, END)
        self.results.insert(0.0, message)


# main
root = Tk()
root.title("Airfare Estimator")
root.geometry("565x360")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
