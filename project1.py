import turtle
p = turtle.Turtle()
turtle.bgcolor("gray")
p.shape("classic")

#columns
p.color("blue")
p.penup()
p.goto(-100, 0)
p.pendown()

p.left(90)
p.forward(150)

p.penup()
p.goto(100, 0)
p.pendown()

p.forward(150)


#upperarc
p.left(60)
p.forward(20)

for i in range(2):
    p.left(10)
    p.forward(35)

p.penup()
p.goto(-100, 150)
p.pendown()

p.setheading(90)
p.right(60)
p.forward(20)

for i in range(2):
    p.right(10)
    p.forward(35)
p.setheading(0)
p.forward(30)


#lowerarc
p.penup()
p.goto(-100, 0)
p.pendown()
p.setheading(90)

p.circle(-60, -60)
p.right(180)
p.forward(81)

p.penup()
p.goto(100, 0)
p.pendown()
p.setheading(90)

p.circle(60, -60)
p.left(180)
p.forward(81)


#innerpart(lowpart)
p.color("gold")
p.penup()
p.goto(-80, 0)
p.pendown()
p.setheading(90)

p.circle(-45, -40)
p.right(160)
p.forward(80)

p.penup()
p.goto(80, 0)
p.pendown()
p.setheading(90)

p.circle(45, -40)
p.left(160)
p.forward(80)


#innerpart(highpart)
p.penup()
p.goto(-80, 0)
p.pendown()
p.setheading(0)
p.left(90)
p.forward(45)

p.penup()
p.goto(80, 0)
p.pendown()
p.setheading(0)
p.left(90)
p.forward(90)

p.setheading(180)
p.circle(310, 31.1)


#text
p.penup()
p.goto(-50, 120)
p.pendown()
p.color("white")
p.write("AMITY", font=("Times New Roman", 30))

p.penup()
p.goto(-49, 105)
p.pendown()
p.color("white")
p.write("UNIVERSITY", font=("Times New Roman", 16))


#torch
p.color("black")
p.penup()
p.goto(15, -60)
p.pendown()
p.setheading(0)
p.left(120)
p.forward(40)

p.penup()
p.goto(30, -51)
p.pendown()

p.setheading(0)
p.left(90)
p.forward(40)

p.setheading(90)
p.circle(20.5, -135)


#fire
p.penup()
p.goto(27, 5)
p.pendown()
p.setheading(90)

p.color("white")
p.width(3)
p.circle(21, -220)
p.circle(-40, -72)
p.circle(-17, 110)
p.circle(15, 120)

p.penup()
p.goto(300, 300)

turtle.done()