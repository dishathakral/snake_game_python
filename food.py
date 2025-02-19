from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.penup()
        self.color('blue')
        self.shape('circle')
        self.shapesize(0.8,0.8)
        self.speed('slow')
        self.food_location()

    def food_location(self):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        self.teleport(x, y)



