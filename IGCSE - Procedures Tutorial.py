import turtle
def triangle(size,num,y):
  turtle.speed(0)
  turtle.penup()
  turtle.goto(-350, y)
  turtle.pendown()
  for i in range (4):
    y = y - 100
    for i in range(num):
      turtle.forward(size) 
      turtle.left(120)
      turtle.forward(size)
      turtle.left(120)
      turtle.forward(size)
      turtle.left(120)
      turtle.penup()
      turtle.forward(size+20)
      turtle.pendown()
    turtle.penup()
    turtle.goto(-350, y)
    turtle.pendown()
triangle(100, 6, 100)
