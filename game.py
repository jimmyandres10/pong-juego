import turtle
import winsound



#WINDOW
window = turtle.Screen()
window.title("game pong")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0)

#scorenum

score_a = 0
score_b = 0





#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball

ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

#score board
score = turtle.Turtle()
score.speed(0)
ball.shape("square")
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player red: {}   Player blue: {} ".format(score_a, score_b), align="center", font=("courier", 24, "normal"))




#funciones movimiento paleta a

def paddle_a_up():
    y = paddle_a.ycor()

    if( y < 230):
        y += 20

    paddle_a.sety(y)


def paddle_a_down():

    y = paddle_a.ycor()

    if( y > -230):
        y -= 20

    paddle_a.sety(y)



#funciones movimiento paleta b

def paddle_b_up():
    y = paddle_b.ycor()

    if( y < 230):
        y += 20

    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()

    if( y > -230):
        y -= 20

    paddle_b.sety(y)


window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")

window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


while True:
    window.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("son1.mp3",winsound.SND_ASYNC)


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("son1.mp3",winsound.SND_ASYNC)

    
    if ball.xcor() > 390:
        ball.goto(0,0)
        score_a += 1
        score.clear()
        score.write("Player Purple: {}   Player blue: {} ".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        winsound.PlaySound("son2.mp3",winsound.SND_ASYNC)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        score_b += 1
        score.clear()
        score.write("Player Purple: {}   Player blue: {} ".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        winsound.PlaySound("son2.mp3",winsound.SND_ASYNC)
        ball.dx *= -1


    if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("son1.mp3",winsound.SND_ASYNC)


    if(ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("son1.mp3",winsound.SND_ASYNC)