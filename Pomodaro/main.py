from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = ""
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    heading.config(text='Timer')
    tick.config(text='')
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 2 != 0:
        heading.config(text="Work", fg=GREEN)
        count_down(work_sec)

    elif REPS % 2 == 0 and REPS % 8 != 0:
        heading.config(text="Break", fg=PINK)
        count_down(short_break)

    elif REPS % 8 == 0:
        heading.config(text="Break", fg=RED)
        count_down(long_break)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS/2)
        for i in range(work_session):
            marks += '✔'

        tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 120, image=tomato_image)
timer_text = canvas.create_text(100, 140, text='00:00', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1)

heading = title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title.grid(row=0, column=1)

start_button = Button(text='Start', width=5, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', width=5, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

tick = check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)

window.mainloop()
