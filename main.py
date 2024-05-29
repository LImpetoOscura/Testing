import turtle

#Change the background color to black
turtle.bgcolor("black")

#Adjust speed of Turtle (lower=faster)
turtle.speed(0)

#Create a list of colors
colors=["#710C04","#900603","#900D09","#9B1003","#710C04"]

#Counter variables
colorNum=0
size=1

#Change this variable to control how many sides your shape will have
sides=4


#Draw the spiral
#This loops forever
while(True):
  colorNum=colorNum+1
  for i in range (sides):
    turtle.forward(size)
    turtle.right(360/sides + 1)
    size=size + 1
  turtle.color(colors[colorNum%5])