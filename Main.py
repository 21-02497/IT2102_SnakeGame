from tkinter import Label, ALL, Tk, Canvas
import random
import sys
import os

from Utilities import Util
from Snakes import Snake
from Foods import Food

def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= Util.SPACE_SIZE
    elif direction == "down":
        y += Util.SPACE_SIZE
    elif direction == "left":
        x -= Util.SPACE_SIZE
    elif direction == "right":
        x += Util.SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = Util.canvas.create_rectangle(x, y, x + Util.SPACE_SIZE, y + Util.SPACE_SIZE, fill=Util.SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        Util.canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        Util.canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        Util.window.after(Util.SPEED, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= Util.GAME_WIDTH:
        return True
    elif y < 0 or y >= Util.GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    Util.canvas.delete(ALL)
    Util.canvas.create_text(Util.canvas.winfo_width()/2, Util.canvas.winfo_height()/3,
                        font=('consolas',70), text="GAME OVER!", fill="red", tag="gameover")
    Util.canvas.create_text(Util.canvas.winfo_width()/2, Util.canvas.winfo_height()/2,
                        font=('consolas',30), text="Press 'r' to Restart", fill="red", tag="gameover")
    Util.canvas.create_text(Util.canvas.winfo_width()/2, Util.canvas.winfo_height()/1.5,
                        font=('consolas',30), text="Press ESC to Quit.", fill="red", tag="gameover")

def close(event):
    sys.exit()

def restart(event):
    Util.window.destroy()
    os.startfile(r'C:\Users\Acer\Desktop\2nd-year\Docus\python files\final_proj new\Snake.py')

Util.window.title("Snake game")
Util.window.resizable(False, False)

score = 0
direction = 'down'

label = Label(Util.window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

Util.canvas.pack()

Util.window.update()

window_width = Util.window.winfo_width()
window_height = Util.window.winfo_height()
screen_width = Util.window.winfo_screenwidth()
screen_height = Util.window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

Util.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

Util.window.bind('<Left>', lambda event: change_direction('left'))
Util.window.bind('<Right>', lambda event: change_direction('right'))
Util.window.bind('<Up>', lambda event: change_direction('up'))
Util.window.bind('<Down>', lambda event: change_direction('down'))
Util.window.bind('<Escape>', close)
Util.window.bind('<r>', restart)

snake = Snake()
food = Food()

next_turn(snake, food)

Util.window.mainloop()
