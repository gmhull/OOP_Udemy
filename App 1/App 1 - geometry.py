import random, turtle

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_point(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and \
            rectangle.point1.y < self.x < rectangle.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        x_dist = self.x - point.x
        y_dist = self.y - point.y
        return (x_dist**2 + y_dist**2) ** 0.5

    def str(self):
        print(self.x, "")


class Rectangle(object):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def check_area(self, guess):
        area = ((self.point2.x - self.point1.x) * (self.point2.y - self.point1.y))
        print(area)
        if guess == area:
            return True
        else:
            return False

    def str(self):
        print(self.point1)
        print(self.point2)


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.goto(self.point1.x, self.point2.y)
        canvas.goto(self.point2.x, self.point2.y)
        canvas.goto(self.point2.x, self.point1.y)
        canvas.goto(self.point1.x, self.point1.y)

class GuiPoint(Point):
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)



if __name__ == '__main__':
    rect = GuiRectangle(Point(random.randint(0,400),random.randint(0,400)), \
        Point(random.randint(10,400),random.randint(10,400)))
    print("Rect. Coordinates: ", rect.point1.x, ", ", rect.point1.y, \
        " and ", rect.point2.x, ", ", rect.point2.y)
    user_point = GuiPoint(float(input("Guess X: ")),float(input("Guess Y: ")))

    user_area = float(input("What is the area? "))

    print(user_point.check_point(rect))
    print(rect.check_area(user_area))

    myturtle = turtle.Turtle()
    rect.draw(canvas=myturtle)
    user_point.draw(canvas=myturtle)

    turtle.done()
