from tkinter import *

#MAKE THE WINDOW
window = Tk()
window.title("Miles to km converter")
window.minsize(height=100, width=250)
window.config(padx=10, pady=10)

#MILES LABEL
miles_label = Label(text="Miles", font=("Ariel", 10, "bold"))
miles_label.config(text="Miles")
miles_label.grid(column=3, row=1)

#MILES INPUT
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=2, row=1)

#IS EQUAL LABEL
equal_label = Label(text="Is equal to", font=("Ariel", 10, "bold"))
equal_label.grid(column=0, row=2)

#KM LABEL
km_label = Label(text="Kilometers", font=("Ariel", 10, "bold"))
km_label.grid(column=3, row=2)

#KM INPUT
km_input = Entry(width=10)
km_input.insert(END, string="0")
km_input.grid(column=2, row=2)

#CONVERSION BUTTON
def convert_button():
    miles = miles_input.get()
    conv_miles = int(miles)
    conversion = round(conv_miles * 1.60934)
    km_input.delete(0, END)
    km_input.insert(END, string=str(conversion))
    return conversion

button = Button(text="Convert", command=convert_button)
button.config(padx=10, pady=10)
button.grid(column=2, row=3)



























window.mainloop()