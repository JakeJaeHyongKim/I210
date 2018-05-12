from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Estimate Your Loan:").grid(row = 0, column = 1)
        Label(self, text = "Customer Name:").grid(row = 1, column = 0, sticky = E)
        Label(self, text = "Customize the Car:").grid(row = 2, column = 1)
        Label(self, text = "Choose Brand:").grid(row = 3, column = 0)
        Label(self, text = "Choose Type:").grid(row = 3, column = 1)       
        Label(self, text = "Choose Options:").grid(row = 3, column = 2)     
        Label(self, text = "Money Down:").grid(row = 8, column = 1)

        self.brand = StringVar()
        self.brand.set("Ford")
        Radiobutton(self, text="Ford ($18,000)", value="Ford", variable=self.brand).grid(row=4, column=0, sticky=W)
        Radiobutton(self, text="Nissan ($26,000)", value="Nissan", variable=self.brand).grid(row=5, column=0, sticky=W)
        Radiobutton(self, text="BMW ($40,000)", value="BMW", variable=self.brand).grid(row=6, column=0, sticky=W)
        Radiobutton(self, text="Tesla ($50,000)", value="Tesla", variable=self.brand).grid(row=7, column=0, sticky=W)
        
        self.type = StringVar()
        self.type.set("budget")
        Radiobutton(self, text="Budget (-15%)", value="budget", variable=self.type).grid(row=4, column=1)
        Radiobutton(self, text="Mid-Range (+5%)", value="mid-range", variable=self.type).grid(row=5, column=1)
        Radiobutton(self, text="Luxury (+20%)", value="luxury", variable=self.type).grid(row=6, column=1)

        self.name = Entry(self, width=40)
        self.name.grid(row=1, column=1, sticky=W)

        self.down = Entry(self, width=10)
        self.down.grid(row=9, column=1)
        
        self.alloy = BooleanVar()
        Checkbutton(self, text = "Alloy Wheels (+$1,000)", variable = self.alloy).grid(row = 4, column = 2, sticky = W)
        self.leather = BooleanVar()
        Checkbutton(self, text = "Leather Interior (+$2,000)", variable = self.leather).grid(row = 5, column = 2, sticky = W)
        self.satellite = BooleanVar()
        Checkbutton(self, text = "Satellite Radio (+$500)", variable = self.satellite).grid(row = 6, column = 2, sticky = W)

        self.calculator = PhotoImage(file="calculator.gif")
        Button(self, image = self.calculator, command=self.calculate).grid(row = 1, column = 2)

        self.results = Text(self, width=70, height=6, wrap = WORD)
        self.results.grid(row = 10, column = 0, columnspan = 3)

    def calculate(self):

        message = "Thanks for shopping with us, " + self.name.get() + ".\n"

        message += "Your car is a " + self.type.get() + " " + self.brand.get()

        options = []
        add_on = 0

        if self.alloy.get():
            options.append("alloy wheels")
            add_on += 1000
        if self.leather.get():
            options.append("leather seats")
            add_on += 2000
        if self.satellite.get():
            options.append("satellite radio")
            add_on += 500

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

        brand = self.brand.get()

        if brand == "Ford":
            price = 18000
        elif brand == "Nissan":
            price = 26000
        elif brand == "BMW":
            price = 40000
        else:
            price = 50000

        grade = self.type.get()

        if grade == "budget":
            price *= .85
        elif grade == "mid-range":
            price *= 1.05
        else:
            price *= 1.2

        final = round(price + add_on, 2)

        message += "The total price is $" + str(final) + "\n"

        loan = round(final - float(self.down.get()), 2)

        message += "You will need to borrow $" + str(loan) + "\n"

        payment = round((loan * 1.05) / 48, 2)

        message += "At 5% interest, over 4 years of payments, your monthly payment will be $" + str(payment)

        self.results.delete(0.0, END)
        self.results.insert(0.0, message)


# main
root = Tk()
root.title("Car Loan Estimator")
root.geometry("565x370")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
