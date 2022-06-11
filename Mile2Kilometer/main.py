from tkinter import *


def calculate_on_click():
    miles = int(input_column.get())
    km = miles * 1.60
    km = str(km)
    output_text.config(text=km)


window = Tk()
window.minsize(width=300, height=200)
window.title('Mile to Km Converter')
window.config(padx=50, pady=50)

input_column = Entry(width=10)
input_column.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_text = Label(text="is equals to")
equal_text.grid(row=1, column=0)

output_text = Label(text="0")
output_text.grid(row=1, column=1)

km_text = Label(text='KM')
km_text.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate_on_click)
button.grid(row=2, column=1)

window.mainloop()
