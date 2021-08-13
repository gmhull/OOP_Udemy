"""
Title: Math Painter
Description: An app that allow the user to provide start coordinats of shapes
and their dimensions, color.  The program will produce an image with the shapes
in the given location.
"""
import numpy as np
from PIL import Image
import os
from canvas import Canvas
from shapes import Square, Rectangle


if __name__ == "__main__":
    canvas_width = int(input("Enter desired canvas width: "))
    canvas_height = int(input("Enter desired canvas height: "))
    color_r = int(input("How much red should the canvas have? "))
    color_g = int(input("How much green? "))
    color_b = int(input("How much blue? "))
    canvas = Canvas(color=(color_r, color_g, color_b), height=100, width=100)

    while True:
        shape_type = input("would you like to draw a square or rectangle? Or type quit to exit. ")

        if shape_type.lower() == 'square':
            square_x = int(input("Enter x value of the square: "))
            square_y = int(input("Enter y value of the square: "))
            square_length = int(input("Enter side length of the square: "))
            square_color_r = int(input("How much red should the square have? "))
            square_color_g = int(input("How much green? "))
            square_color_b = int(input("How much blue? "))
            square_color = (square_color_r, square_color_g, square_color_b)
            sq = Square(square_x, square_y, square_length, square_color)
            sq.draw(canvas)

        if shape_type.lower() == 'rectangle':
            rectangle_x = int(input("Enter x value of the rectangle: "))
            rectangle_y = int(input("Enter y value of the rectangle: "))
            rectangle_width = int(input("Enter width of the rectangle: "))
            rectangle_height = int(input("Enter height of the rectangle: "))
            rectangle_color_r = int(input("How much red should the rectangle have? "))
            rectangle_color_g = int(input("How much green? "))
            rectangle_color_b = int(input("How much blue? "))
            rectangle_color = (rectangle_color_r, rectangle_color_g, rectangle_color_b)
            rect = Rectangle(rectangle_x, rectangle_y, rectangle_width, rectangle_height, rectangle_color)
            rect.draw(canvas)

        if shape_type.lower() == 'quit':
            break

    canvas.create('canvas.png')
