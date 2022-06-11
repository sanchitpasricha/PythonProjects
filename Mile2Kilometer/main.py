from tkinter import *

def button_click():
    user_input = input.get()
    label.config(text=user_input)


window = Tk()
window.title("Mile To Kilometer Converter")
window.minsize(width=500, height=300)

label = Label(text="I am a label", font=("Arial", 24, "bold"))
label.pack(expand=True)


input = Entry(width=10)
input.pack()

button = Button(text="Click me", command=button_click)
button.pack()

window.mainloop()
