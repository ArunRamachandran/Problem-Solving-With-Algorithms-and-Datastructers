import turtle

#my_turtle = turtle.Turtle()
#my_win = turtle.Screen()

def tree(br_l, t) :
	if br_l > 5:
		t.forward(br_l)
		t.color("brown") #
		t.right(20)
		tree(br_l - 15, t)
		t.left(40)
		t.color("brown")
		tree(br_l - 10, t)
		t.color("green") #
		#t.color("brown") #
		t.right(20)
		t.backward(br_l)
		t.color("brown") #

def main() :
	t = turtle.Turtle()
	my_win = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color("brown") #
	tree(75, t)

main()
#tree(100, my_turtle)
#my_win.exitonclick()
