from tkinter import Tk, Canvas

class Util:

    GAME_WIDTH = 600
    GAME_HEIGHT = 600
    SPEED = 150
    SPACE_SIZE = 20
    BODY_PARTS = 3
    SNAKE_COLOR = "#FEDD59"
    FOOD_COLOR = "#FF0000"
    BACKGROUND_COLOR = "#000000"

    window = Tk()
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
