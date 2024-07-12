from turtle import*

#we want to paint a house

#step 1: draw a square

speed(50)
width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("red")
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup
goto(0,200)
pendown

color("yellow")
left(120)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)

penup()
goto(200,200)
pendown()

left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

penup()
goto(0,170)
pendown()

right(90)
forward(60)

penup()
goto(30,140)
pendown()

left(90)
forward(60)

penup()
goto(170,140)
pendown()

forward(60)

penup()
goto(140,170)
pendown()

right(90)
forward(60)

penup()
goto(0,200)
pendown()

color("green")

left(180)
forward(300)
left(90)
forward(200)
left(90)
forward(300)

penup()
goto(-210,0)
pendown()

color("brown")
left(90)
forward(120)
right(90)
forward(120)
right(90)
forward(120)
right(90)
forward(120)

penup()
goto(-290,120)
pendown()

color("cyan")
right(180)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)

penup()
goto(-80,120)
pendown()

right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)

penup()
goto(-290,85)
pendown()

right(90)
forward(70)

penup()
goto(-255,120)
pendown()

right(90)
forward(70)

penup()
goto(-80,85)
pendown()

left(90)
forward(70)

penup()
goto(-45,120)
pendown()

right(90)
forward(70)


exitonclick()