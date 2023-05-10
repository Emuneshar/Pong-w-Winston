import turtle
import os 

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

score_left = 0
score_right = 0

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("blue")
ball.shapesize(0.5, 0.5)

paddleOne = turtle.Turtle()
paddleOne.penup()


paddleTwo = turtle.Turtle()
paddleTwo.penup()



