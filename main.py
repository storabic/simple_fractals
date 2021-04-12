import turtle
import random

MIN_BRANCH_LEN = 20
SHORTEN_BY = 10
ANGLE = 30

def change_color(drawer):
    R = random.random()
    B = random.random()
    G = random.random()

    drawer.color(R, G, B)

def build_tree(drawer, branch_len):
    if (branch_len > MIN_BRANCH_LEN):
        change_color(drawer)
        drawer.forward(branch_len)
        new_len = branch_len - SHORTEN_BY

        drawer.left(ANGLE)
        build_tree(drawer, new_len)

        drawer.right(ANGLE * 2)
        build_tree(drawer, new_len)

        drawer.left(ANGLE)
        drawer.backward(branch_len)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.setheading(90)
drawer.speed(8)

build_tree(drawer, 100)
drawer.mainloop()
