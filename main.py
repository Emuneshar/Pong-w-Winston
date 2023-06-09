import turtle
import os 

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
#window.tracer(0)

score_left = 0
score_right = 0

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("blue")
ball.goto(0,0)

paddleOne = turtle.Turtle()
paddleOne.penup()
paddleOne.speed(0)
paddleOne.shape("square")
paddleOne.shapesize(stretch_len = -1, stretch_wid = 5)
paddleOne.color("red")
paddleOne.goto(350, 0)


paddleTwo = turtle.Turtle()
paddleTwo.penup()
paddleTwo.speed(0)
paddleTwo.shape("square")
paddleTwo.shapesize(stretch_len = -1, stretch_wid = 5)
paddleTwo.color("green")
paddleTwo.goto(-350, 0)


while True:
  window.update()

