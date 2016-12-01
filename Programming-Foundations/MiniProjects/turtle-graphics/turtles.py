import turtle
def ocean():
	window = turtle.Screen()
	window.bgcolor("blue")

def draw_square(turt):
	turt.shape("turtle")
	turt.color("white")
	turt.forward(100)
	for i in range(3):
		turt.forward(50)
		turt.right(90)


def draw_circle():

	setty = turtle.Turtle()
	setty.shape("turtle")
	setty.color("black")
	setty.speed(2)

	setty.circle(100)

def draw_triangle():

	grandma = turtle.Turtle()
	grandma.shape("turtle")
	grandma.color("black")
	grandma.speed(1)

	for i in range(3):
		grandma.forward(100)
		grandma.right(120)

def donut():
	bill = turtle.Turtle()
	for i in range(360):
		draw_square(bill)
		bill.speed(i+1)
		bill.right(1)
ocean()
donut()
window.exitonclick()


