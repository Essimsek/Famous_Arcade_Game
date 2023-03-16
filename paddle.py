from turtle import Turtle
PLAYER_1_POS = (-360, 0)
PLAYER_2_POS = (350, 0)

class Paddle(Turtle):
	def __init__(self, player: int):
		super().__init__()
		self.player = player
		self.shape("square")
		self.color("white")
		self.penup()
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.set_paddle_position()


	def set_paddle_position(self) -> None:
		if self.player == 1:
			self.goto(PLAYER_1_POS)
		else:
			self.goto(PLAYER_2_POS)

	def move_up(self) -> None:
		if self.ycor() < 240:
			new_y = self.ycor() + 20
			self.goto(x=self.xcor(), y=new_y)

	def move_down(self) -> None:
		if self.ycor() > -240:
			new_y = self.ycor() - 20
			self.goto(x=self.xcor(), y=new_y)
