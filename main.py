import turtle

drawingBoard = turtle.Screen()
drawingBoard.bgcolor("light blue")
drawingBoard.title("Catch the turtle")
drawingBoard.addshape("pic.gif")
turtle.shape("pic.gif")

myTurtle = turtle.Turtle(visible=False) #fare iconunu gorunmez yapar
turtle.penup() #cizgiyi gorunmez yapar


turtle.ht()
turtle.setposition(100, 100)
turtle.st()
turtle.ht()
turtle.setposition(200, 150)
turtle.st()




turtle.mainloop()