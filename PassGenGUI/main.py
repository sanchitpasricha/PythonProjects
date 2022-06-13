from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title='Clipboard', message='Password Copied to Clipboard !')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_in_file():
    web = web_entry.get()
    email = mail_entry.get()
    password = pass_entry.get()

    if len(web) == 0 and len(password) == 0:
        messagebox.askokcancel(title='Empty Fields', message="You have left email or password field empty")
    else:
        is_ok = messagebox.askokcancel(title=web,
                                       message=f'Please check the details:\nEmail:{email}\nPassword:{password}\n'
                                               f'Press ok to confirm')
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f'{web} | {email} | {password} \n')
        web_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=20, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

webite_label = Label(text="Website:", bg='white', fg='black')
webite_label.grid(row=1, column=0)

web_entry = Entry(width=35, bg='white', highlightthickness=0, fg='black')
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

mail_label = Label(text="Email/Username:", bg='white', fg='black')
mail_label.grid(row=2, column=0)

mail_entry = Entry(width=35, bg='white', highlightthickness=0, fg='black')
mail_entry.insert(0, 'sanchit0229@gmail.com')
mail_entry.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:", bg='white', fg='black')
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=20, bg='white', fg='black', highlightthickness=0)
pass_entry.grid(row=3, column=1)

generate_button = Button(text='Generate Password', width=11, highlightbackground='white', command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=33, highlightbackground='white', command=save_in_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
