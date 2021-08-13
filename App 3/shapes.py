import numpy as np
from PIL import Image

class Square(object):
    """Provide the parameters for a square and draw it."""

    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.width = length
        self.height = length
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y:self.y+self.height, self.x:self.x+self.width] = self.color

class Rectangle(object):
    """Provide the parameters for a rectangle and draw it."""

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y:self.y+self.height, self.x:self.x+self.width] = self.color
