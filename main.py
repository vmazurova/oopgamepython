from tkinter import *

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50 #snake class
SPACE_SIZE = 50
BODY_PARTS = 3 #snake class
SNAKE_COLOR = "#8532a8" #snake class
FOOD_COLOR = "#f5cc02" #jidlo class
BACKGROUND_COLOR = "#000000"

class Snake():
    def __init__(self, color, body, speed):
        self.color = SNAKE_COLOR
        self.body = BODY_PARTS
        self.speed = SPEED

class Food():
    def __init__(self, color):
        self.color = FOOD_COLOR

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collision():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake Hra")
window.resizable(False, False)
score = 0
label = Label(text="Score{}".format(score))
window.geometry("700x700")
window.mainloop()
