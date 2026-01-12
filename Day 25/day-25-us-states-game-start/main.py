import turtle
import pandas

# Set up game
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Read data
data = pandas.read_csv("50_states.csv")

#Convert to list
states_remaining_list = data["state"].to_list()

#Use score for loop and game logic until user guesses all states
score = 0
guessed_states = []
while score != 50:
    # Get user answer
    input_title = ""
    if score == 0:
        input_title = "Guess the State"
    else:
        input_title = f"{score}/50 States Correct"
    answer_state = screen.textinput(title = input_title, prompt="What's another state's name?")
    answer_state = answer_state.title()

    # Secret code to exit game
    if answer_state == "Exit":
        break
    # Check if answer in list, add to map and remove from list if correct
    elif answer_state in states_remaining_list:
        states_remaining_list.remove(answer_state)
        score += 1
        guessed_states.append(answer_state)

        # get coordinates from data
        x_cor = data[data["state"] == answer_state]["x"].tolist()[0]  # whole method implemented for getting x coordinate
        y_cor = data[data["state"] == answer_state]["y"].tolist()[0]  # whole method implemented for getting y coordinate

        # Write correct guesses onto map
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.goto(x_cor, y_cor)
        text.write(answer_state)

# Save missing states to csv
# states_to_learn.csv
data_dict = {
    "Missing States": states_remaining_list
}

export_data = pandas.DataFrame(data_dict)
print(export_data)
export_data.to_csv("states_to_learn.csv")