from turtle import Turtle, Screen
from snake_game import *
from tkinter import *
import random


def gaming():
    win = Tk()
    win.geometry("200x90")
    win.title("Games")

    # --------------------------------------------- TURTLE GAME ------------------------------------------------
    def turtle_game():
        while True:
            is_game_on = False
            screen = Screen()
            screen.setup(width=500, height=350)
            user_input = screen.textinput(title="Make your bet",
                                          prompt="Guess which turtle will win \n\npurple, blue, green, yellow, orange, red\n\nEnter a color:")
            turtle_color = ['purple', 'blue', 'green', "yellow", "orange", 'red']
            all_turtles = []

            for t in range(6):
                new_turtle = Turtle("turtle")
                new_turtle.color(turtle_color[t])
                new_turtle.penup()
                new_turtle.goto(x=-230, y=-60 + (30 * t))
                all_turtles.append(new_turtle)

            if user_input:
                is_game_on = True

            while is_game_on:
                for turtle in all_turtles:
                    random_num = random.randint(0, 10)
                    turtle.forward(random_num)
                    if turtle.xcor() > 230:
                        is_game_on = False
                        winning_color = turtle.pencolor()
                        if user_input == winning_color:
                            # print(f"You've won! The {winning_color} is the winner!")
                            game_over = screen.textinput(title=f"You've won! The {winning_color} is the winner!",
                                                         prompt="Play again? - ")
                            if game_over == "no":
                                screen.exitonclick()
                            if game_over == "yes":
                                continue
                        else:
                            # print(f"You've lost! The {winning_color} is the winner!")
                            game_over = screen.textinput(title=f"You've lost! The {winning_color} is the winner!",
                                                         prompt="Play again? (yes/no) - ")
                            if game_over == "no":
                                screen.exitonclick()
                            if game_over == "yes":
                                continue

            # screen.exitonclick()

    def quit_games():
        win.destroy()
        window.destroy()

    Button(win, text="Snake Game 🐍", command=snake_game, fg="yellow", width=9, height=1).pack()
    Button(win, text="Turtle Race 🐢", command=turtle_game, fg="red", width=9, height=1).pack()
    Button(win, text="EXIT", command=quit_games, width=7, height=1, fg="red").pack()

    win.mainloop()
