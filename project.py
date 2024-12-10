import turtle
import random
t= turtle.Turtle()
turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("hot pink")
t2=turtle.Turtle()
t2.hideturtle()
t2.penup()
t.penup()
t.goto(0,70)


#Intro
t.write("Intro", font=('lora', 40, 'bold'), align="center")
t.goto(0,45)
t.write("Laela Markwood", font=('lora', 20, 'bold'), align="center")





turtle.addshape("intro.gif")

t2.shape("intro.gif")

t2.goto(150, -150)
a = t2.stamp()
t2.goto(0,0)

t.penup()
t.goto(150,-220)




turtle.addshape("me.gif")

t2.shape("me.gif")

t2.goto(-150, -150)
a = t2.stamp()
t2.goto(0,0)


t.penup()
t.goto(-150,-230)






t.goto(0, 200)

t.pencolor('red')
t.fillcolor('yellow')
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()
t.penup()
t.goto(-100,-100)
t.pendown()
t.setheading(0)
t.pencolor('blue')
t.fillcolor('green')
t.begin_fill()






#FOOD PAGE
enter =input("Press Enter for next page")
t.clear()
screen.bgcolor('light blue')
t.goto(0,0)

t.write("Favorite Foods", font=('lora', 40, 'bold'), align="center")


turtle.addshape("mac.gif")

t2.shape("mac.gif")

t2.goto(150, -150)
a = t2.stamp()
t2.goto(0,0)

t.penup()
t.goto(150,-220)

t.write("mac and cheese", font=('lora', 10, 'bold'), align = "center")

turtle.addshape("fries.gif")

t2.shape("fries.gif")

t2.goto(-150, -150)
a = t2.stamp()
t2.goto(0,0)


t.penup()
t.goto(-150,-230)

t.write("french fries", font=('lora', 10, 'bold'), align = "center")


turtle.addshape("grapes.gif")

t2.shape("grapes.gif")

t2.goto(0,190 )
a = t2.stamp()
t2.goto(0,0)

t.penup()
t.goto(0,120)

t.write("grapes", font=('lora', 10, 'bold'), align = "center")





t.penup()
t.goto(-150,50)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()







enter =input("Press Enter for next page")






#HOBBIE PAGE
enter =input("Press Enter for next page")
t2.clear()
t.clear()


t.goto(0,0)



#HOBBy PAGE
screen.bgcolor('purple')
t.write("Hobbies", font=('lora', 40, 'bold'), align="center")




turtle.addshape("softball.gif")

t2.shape("softball.gif")

t2.goto(150, -150)
a = t2.stamp()
t2.goto(0,0)

t.penup()
t.goto(150,-220)

t.write("softball", font=('lora', 10, 'bold'), align = "center")




turtle.addshape("volleyball.gif")

t2.shape("volleyball.gif")

t2.goto(-150, -150)
a = t2.stamp()
t2.goto(0,0)


t.penup()
t.goto(-150,-230)

t.write("volleyball", font=('lora', 10, 'bold'), align = "center")




turtle.addshape("baking.gif")

t2.shape("baking.gif")

t2.goto(150,200)
a = t2.stamp()
t2.goto(0,0)

t.penup()
t.goto(150,130)

t.write("baking", font=('lora', 10, 'bold'), align = "center")




turtle.addshape("travel.gif")

t2.shape("travel.gif")

t2.goto(-150,200)
a = t2.stamp()
t2.goto(0,0)

t.penup()
t.goto(-150,110)

t.write("traveling", font=('lora', 10, 'bold'), align = "center")





t.penup()
t.goto(-50,100)
t.pendown()
t.begin_fill()
t.fillcolor('purple')
t.goto(50,100)
t.goto(0,200)
t.goto(-50,100)
t.end_fill()
t.penup()








enter =input("Press Enter for next page")

#MOVIE PAGE
enter =input("Press Enter for next page")
t.clear()
t2.clear()
screen.bgcolor('orange')
t.goto(0,0)
t.write("Favorite Movie", font=('lora', 40, 'bold'), align="center")






turtle.addshape("sandlot.gif")

t2.shape("sandlot.gif")

t2.goto(150, -150)
a = t2.stamp()
t2.goto(0,0)

t.penup()
t.goto(150,-220)

t.write("The Sandlot", font=('lora', 10, 'bold'), align = "center")





turtle.addshape("mystery.gif")

t2.shape("mystery.gif")

t2.goto(-150, -140)
a = t2.stamp()
t2.goto(0,0)


t.penup()
t.goto(-150,-230)

t.write("Murder Mystery", font=('lora', 10, 'bold'), align = "center")





t.penup()
t.goto(-100,100)
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.end_fill()
t.penup()








enter =input("Press Enter for next page")


#SPORT PAGE
enter =input("Press Enter for next page")
t.clear()
t2.clear()
t.goto(0,0)
screen.bgcolor('yellow')
t.write("Favorite Sport", font=('lora', 40, 'bold'), align="center")







turtle.addshape("softball.gif")

t2.shape("softball.gif")

t2.goto(150, -150)
a = t2.stamp()
t2.goto(0,0)

t.penup()
t.goto(150,-220)

t.write("softball", font=('lora', 10, 'bold'), align = "center")




turtle.addshape("softball2.gif")

t2.shape("softball2.gif")

t2.goto(-150, -150)
a = t2.stamp()
t2.goto(0,0)


t.penup()
t.goto(-150,-230)

t.write("softball", font=('lora', 10, 'bold'), align = "center")






t.penup()
t.goto(130,100)
t.pendown()
t.fillcolor('cornsilk')
t.begin_fill()
t.right(60)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.end_fill()
t.penup()









turtle.done()