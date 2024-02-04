from turtle import *

#we want to paint a house 

#step 1:  drow a square
speed(20)
width(7)
color("blue")
forward(225)
left(90)

forward(225)
left(90)

forward(225)
left(90)

forward(225)
left(90)
#end of square 

#drawing a door

forward(75)
left(90)

color('red')
begin_fill()
forward(120)  #heught of the door 
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(225, 225)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(114)   
forward(212)
end_fill()

penup()
goto(20, 150)
pendown()
left(126)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
penup()
goto(150, 150)
pendown()
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)








exitonclick()