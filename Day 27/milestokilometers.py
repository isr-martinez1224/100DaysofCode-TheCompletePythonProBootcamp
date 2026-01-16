from tkinter import *
from math import ceil

#9x9 grid
#4 labels
#input
#1 button
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


#Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)

answer_label = Label(text=0)
answer_label.grid(column=1, row=1)

km_label = Label(text="Kilometers")
km_label.grid(column=2, row=1)


#Button
def button_clicked():
    km = float(input.get()) * 1.609344
    km = ceil(km)
    answer_label.config(text=km)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


#Entry
input = Entry(width=10)
input.grid(column=1, row=0)
input.insert(END, string="0")


#Must always be at the end
window.mainloop()