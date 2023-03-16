from turtle import Turtle

FONT = ("courier", 60, "normal")


class ScoreBoard:
	def __init__(self):
		self.lines = Turtle()
		self.middle = Turtle()
		self.scores = Turtle()
		self.player_1_score = 0
		self.player_2_score = 0
		self.init_scores()  # assignment
		self.draw_circle()  # draw a circle in the middle
		self.draw_lines()  # draw dashed lines at the middle of the screen

	def draw_lines(self):
		self.lines.pencolor("white")
		self.lines.penup()
		self.lines.goto(x=0, y=280)
		self.lines.pendown()
		self.lines.setheading(270)
		self.lines.pensize(4)
		while self.lines.ycor() > -280:
			self.lines.forward(15)
			self.lines.penup()
			self.lines.forward(15)
			self.lines.pendown()
		self.lines.penup()
		self.lines.hideturtle()

	def draw_circle(self):
		self.middle.color("blue")
		self.middle.penup()
		self.middle.goto(0, -50)
		self.middle.pendown()
		self.middle.circle(50)
		self.middle.hideturtle()

	def init_scores(self):
		self.scores.penup()
		self.scores.color("white")
		self.scores.goto(-100, 200)
		self.scores.write(f"{self.player_1_score}", align="center", font=FONT)
		self.scores.goto(100, 200)
		self.scores.write(f"{self.player_2_score}", align="center", font=FONT)
		self.scores.hideturtle()

	def write_scores(self):
		self.scores.clear()
		self.scores.goto(-100, 200)
		self.scores.write(f"{self.player_1_score}", align="center", font=FONT)
		self.scores.goto(100, 200)
		self.scores.write(f"{self.player_2_score}", align="center", font=FONT)


	def game_over(self):
		self.lines.clear()
		self.middle.clear()
		self.scores.goto(0, 0)
		if self.player_1_score == 5:
			self.scores.write(f"player to the left won the game", align="center", font=30)
		else:
			self.scores.write(f"player to the right won the game", align="center", font=30)

