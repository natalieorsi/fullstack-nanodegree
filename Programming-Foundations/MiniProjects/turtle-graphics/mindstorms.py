import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("blue")
	jaime = turtle.Turtle()
	jaime.shape("turtle")
	jaime.color("green")
	jaime.speed(1)
	for i in range(4):
		jaime.forward(150)
		jaime.right(89.99)

	window.exitonclick()
draw_square()