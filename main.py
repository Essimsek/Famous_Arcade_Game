import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

#  Create The Screen
screen = Screen()
screen.title("Arcade Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

#  Initializing
player_1 = Paddle(1)  # Left
player_2 = Paddle(2)  # Right
ball = Ball()
scoreboard = ScoreBoard()


# Key handling
screen.listen()
screen.onkeypress(fun=player_1.move_up, key="w")
screen.onkeypress(fun=player_1.move_down, key="s")
screen.onkeypress(fun=player_2.move_up, key="Up")
screen.onkeypress(fun=player_2.move_down, key="Down")

game_is_on = True

while game_is_on:

	screen.update()
	time.sleep(0.05)
	ball.move()

	# detect collision with wall
	if ball.ycor() < -280 or ball.ycor() > 280:
		ball.bounce_y()

	# detect collision with left paddle
	if ball.distance(player_1) < 50 and ball.xcor() > -350:
		ball.bounce_x()

	# detect collision with right paddle
	if ball.distance(player_2) < 50 and ball.xcor() < 350:
		ball.bounce_x()

	# detect if the ball goes out of bounds at the edge of the screen
	if ball.xcor() > 380 or ball.xcor() < -380:
		if ball.xcor() > 380:
			scoreboard.player_1_score += 1
		else:
			scoreboard.player_2_score += 1
		ball.reset_position()
		scoreboard.write_scores()

		if scoreboard.player_1_score == 5 or scoreboard.player_2_score == 5:
			scoreboard.game_over()
			game_is_on = False

screen.exitonclick()
