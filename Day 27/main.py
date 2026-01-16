from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #add padding to widgets, can do this individually too


#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))


my_label["text"] = "new text"
my_label.config(text= "New Text")
#my_label.pack()
#my_label.place(x=100, y=200)#to the top left corner 0,0
my_label.grid(column=0, row=0)

#Button
def button_clicked():
    #print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)


# New Button
def button_clicked():
    #print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)


#Entry
input = Entry(width=10)
#input.pack()
print(input.get())
input.grid(column=3, row=2)




#Must always be at the end
window.mainloop()


##########################################################
#Default arguments
# def foo(a, b=4, c=6):
#     print(a, b, c)
# foo(4, 9)


def add(*args):
    #print(args[1]) position does matter
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1,2,3)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make") #prefer using get than kw["name"] so it doesnt crash
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

new_car = Car(make="Nissan", model="Skyline")
print(new_car.model)
#################################################