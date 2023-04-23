import turtle
window = turtle.Screen()
window.bgcolor('yellow')

ball = turtle.Turtle(shape='circle')
ball.up()
ball.goto(0, 200)
ball.y = 0

gravition = 0.1


while True:
    ball.y = ball.y - gravition
    ball.goto(0,ball.ycor()+ball.y)

    if ball.ycor() <= -400:
        ball.y = -ball.y





