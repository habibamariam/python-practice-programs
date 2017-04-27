import turtle


def draw_shapes():
    windows = turtle.Screen()
    windows.bgcolor("Red")
    draw_square()
    draw_circle()
    draw_triangle()


      
def draw_square():
   habi= turtle.Turtle()
   habi.shape("turtle")
   habi.color("violet","green")
   habi.speed(2)
   for i in range(1,5):
        habi.forward(100)
        habi.right(90)
        
        
def draw_circle():
    ahsan = turtle.Turtle()
    ahsan.circle(50)
    ahsan.shape("square")
    ahsan.color("yellow")
   

def draw_triangle():
    habi= turtle.Turtle()
    habi.right(180)
    i=0
    while(i < 3):
        habi.forward(100)
        habi.left(120)
        i=i+1
    windows.exitonclick()
draw_shapes()


