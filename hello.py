import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(" I Love You ❤ ")

# Create the turtle
t = turtle.Turtle()
t.speed(1)
t.hideturtle()
t.penup()
t.color("#ffb6c1")

# Draw 5 closely layered hearts with the "I love you" text
for repeat in range(5):

    scale_x = 12 + repeat * 0.8
    scale_y = 12 + repeat * 0.8
    
    for i in range(0, 361, 3):

        angle = math.radians(i)

        x = 16 * (math.sin(angle) ** 3) * scale_x

        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        ) * scale_y

        t.goto(x, y)

        t.write(
            "I love you",
            align="center",
            font=("Arial", 7, "bold")
        )

# Keep the window open
turtle.done() 