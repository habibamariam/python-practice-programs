import turtle

def draw_square(habi):
     for i in range(1,5):
          habi.forward(100)
          habi.right(90)

def draw_shape():
    windows = turtle.Screen()
    windows.bgcolor("Red")
# drawing the turtlehabi


    habi= turtle.Turtle()
    habi.shape("turtle")
    habi.color("violet","green") 
    habi.speed(9)
    for i in range(1,37):
     draw_square(habi)
     habi.right(10)


    windows.exitonclick()
   
draw_shape()
