from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_card = {}
# --------------------------------RANDOM WORD GENERATOR------------------------------------- #
data = pandas.read_csv('data/french_words.csv')
learn = data.to_dict(orient='records')


def next_card():
    global random_card
    global flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(learn)
    french_word = random_card['French']
    canvas.itemconfig(card_data, text=french_word, fill='black')
    canvas.itemconfig(card_head, text='French', fill='black')
    canvas.itemconfig(canvas_image, image=card_image)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------------FLIP THE CARD-------------------------------------------- #
def flip_card():
    canvas.itemconfig(card_head, text='English', fill='white')
    english_word = random_card['English']
    canvas.itemconfig(card_data, text=english_word, fill='white')
    canvas.itemconfig(canvas_image, image=back_image)


# --------------------------------MAIN WINDOW CODE------------------------------------------ #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file='images/card_back.png')
card_image = PhotoImage(file='images/card_front.png')
canvas_image = canvas.create_image(400, 270, image=card_image)
card_head = canvas.create_text(400, 150, text='Title', font=("Ariel", 40, 'italic'), fill='black')
card_data = canvas.create_text(400, 263, text='word', font=("Ariel", 60, 'bold'), fill='black')
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
cross_button = Button(image=cross_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
cross_button.grid(row=1, column=0)

right_image = PhotoImage(file='images/right.png')
cross_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
cross_button.grid(row=1, column=1)

next_card()

window.mainloop()
