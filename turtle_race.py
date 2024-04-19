from turtle import Turtle, Screen
import random
colors = ["red", "blue", "green", "violet", "yellow", "brown"]

restart = True
while restart:
    screen = Screen()
    screen.setup(width=500, height=450)
    input_text = screen.textinput(title="Make a guess:", prompt="Enter your guess color of turtle: ")
    is_game_start = False
    turtles = []
    i = -100
    for color in colors:
        tim = Turtle(shape="turtle")
        tim.penup()
        tim.color(color)
        tim.goto(x=-230, y=i)
        i += 50
        turtles.append(tim)

    if input_text:
        is_game_start = True

    while is_game_start:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_game_start = False
                winning_turtle_color = turtle.pencolor()
                if winning_turtle_color == input_text:
                    user_input = screen.textinput(title="Want to play again?", prompt=f"You got it right!, The {winning_turtle_color} turtle is the winner.")
                else:
                    user_input = screen.textinput(title="Want to play again?", prompt=f"You lose, The {winning_turtle_color} turtle is the winner.")
                if user_input == 'yes':
                    restart = True
                else:
                    restart = False
            random_dist = random.randint(0, 10)
            turtle.forward(random_dist)
    screen.exitonclick()
