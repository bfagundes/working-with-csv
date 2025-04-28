import turtle
import pandas

screen = turtle.Screen()
screen.title(f"US States Game")

us_states_image_path = "./Files/blank_states_img.gif"
screen.addshape(us_states_image_path)
turtle.shape(us_states_image_path)

IS_GAME_OVER = False
score = 0
errors = 10
turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

while not IS_GAME_OVER:
    states_df = pandas.read_csv("./Files/50_states.csv")

    answer = screen.textinput(title="Guess an State", prompt=f"{errors} chances left. You got {score} right!")
    
    if states_df["state"].str.contains(answer.title()).any():
        
        state_row = states_df[states_df["state"] == answer.title()]
        if not state_row.empty:
            x_coor = state_row["x"].values[0]
            y_coor = state_row["y"].values[0]

        turtle.setx(x_coor)
        turtle.sety(y_coor)
        turtle.write(answer.title(), align="left", font=("Arial", 10, "bold"))
        score += 1

    else:
        errors -= 1

    if score >= 50 or errors <= 0:
        IS_GAME_OVER = True

screen.mainloop()