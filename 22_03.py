from turtle import Turtle, Screen
from random import randint
colours=["red", "yelow", "blue",  "red", "brown", "orange", "purple", "black", "green" ]
t=Turtle()
t.pensize(4)


t.shape("turtle")


for i in range(3):#trian
    
    t.forward(60)
    t.left(-120)
     
for i in range(4):#f1
     t.forward(60)
     t.left(-90)
     
for i in range(5):#f2
     t.forward(60)
     t.left(-72)
 
for i in range(6):#f3
     t.forward(60)
     t.left(-60)
     
for i in range(7):#f4
     t.forward(60)
     t.left(-51.428)
     
for i in range(8):#f5
     t.forward(60)
     t.left(-45)     
 
for i in range(9):#f6
     t.forward(60)
     t.left(-40)
     
for i in range(10):#f7
     t.forward(60)
     t.left(-36)        
     

screen=Screen()
screen.exitonclick()
