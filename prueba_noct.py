from turtle import Turtle, Screen
import random
colours=["red", "green yellow", "sky blue",  "indian red",  "orange red",  "purple", "salmon", "dark olive green", "magenta", "dark orange",  "beige", "royal blue", "dark green","forest green", "firebrick" ]
t=Turtle()
t.pensize(4)


t.shape("turtle")


# Genera valores RGB aleatorios
r = random.random()
g = random.random()
b = random.random()

# Establece el color de la pluma
t.color(r, g, b)
 



i = 2
while i < 8:
  #print(i)
  i += 1
  for x in range(i):
    
    t.pencolor((random.choice(colours)))
    t.forward(60)
    t.left(-360/i)
    
    
        




      





screen=Screen()
screen.exitonclick()


