import turtle
import pandas

data = pandas.read_csv('50_states.csv')
state_list = data['state'].to_list()

screen = turtle.Screen()
screen.title('American Atlas')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=(f"{len(guessed_states)}/50"), prompt="Guess the state").title()

    if answer == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('missing_states.csv')

        break

    if answer in state_list:
        guessed_states.append(answer)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        state_data = data[data.state == answer]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(answer)

screen.mainloop()

