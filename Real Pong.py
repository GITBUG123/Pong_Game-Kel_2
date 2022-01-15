import turtle
import winsound
import random


SCREEN = turtle.Screen()
SCREEN.title ("PONG")
SCREEN.bgcolor ("white")
SCREEN.setup ( width = 805.5, height = 605.5)
SCREEN.tracer(0)

# Deklarasi
poin_player = 0
poin_ai = 0
left_bounce = 0
right_bounce = 0

# Raket Player
raket_player = turtle.Turtle()
raket_player.speed(0)
raket_player.shape("square")
raket_player.shapesize(stretch_wid = 5.5, stretch_len = 1.5)
raket_player.color("black")
raket_player.penup()
raket_player.goto(-350, 0)

# Raket Ai
raket_AI = turtle.Turtle()
raket_AI.speed(0)
raket_AI.shape("square")
raket_AI.shapesize(stretch_wid = 5.5, stretch_len = -1.5)
raket_AI.color("green")
raket_AI.penup()
raket_AI.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("blue")
bola.penup()
bola.goto(0, 0)
bola.dx = random.choice([-1, 1])
bola.dy = random.choice([-.65, .65])

# Title
title = turtle.Turtle()
title.speed(0)
title.color("black")
title.penup()
title.hideturtle()
title.goto(0, 250)
title.write("Player: {}                                                 AI: {}       ".format(poin_player, poin_ai),
                   align="center", font=("Constantia", 24, "normal"))

# Player Scored Announce
Ppoind = turtle.Turtle()
Ppoind.speed(0)
Ppoind.color("black")
Ppoind.penup()
Ppoind.hideturtle()
Ppoind.goto(-200, 20)

# AI Scored Announce
AIpoind = turtle.Turtle()
AIpoind.speed(0)
AIpoind.color("black")
AIpoind.penup()
AIpoind.hideturtle()
AIpoind.goto(200, 20)

# Pembuatan Garis Atas-Tengah-Bawah
#Garis Tengah
midpanel = turtle.Turtle()
midpanel.shape("square")
midpanel.shapesize(stretch_wid = 25.5, stretch_len = .3)
midpanel.color("black", "white")
midpanel.penup()
midpanel.goto(0, 0)
#Garis Atas
toppanel = turtle.Turtle()
toppanel.shape("square")
toppanel.shapesize(stretch_wid = .4, stretch_len = 40.5)
toppanel.color("black")
toppanel.penup()
toppanel.goto(0, 295)
#Garis Bawah
botpanel = turtle.Turtle()
botpanel.shape("square")
botpanel.shapesize(stretch_wid = .4, stretch_len = 40.5)
botpanel.color("black")
botpanel.penup()
botpanel.goto(0, -285)

# raket_player_Up
def raket_player_up():
   if raket_player.ycor() < 220.5:
       y = raket_player.ycor()
       y = y + 50
       raket_player.sety(y)
# raket_player_Down
def raket_player_down():
   if raket_player.ycor() > -220.5:
       y = raket_player.ycor()
       y = y - 50
       raket_player.sety(y)

# raket_AI_Up
def raket_AI_up():
   if raket_AI.ycor() < 230.5:
       y = raket_AI.ycor()
       y = y + 5
       raket_AI.sety(y)
# raket_AI_Down
def raket_AI_down():
   if raket_AI.ycor() > -230.5:
       y = raket_AI.ycor()
       y = y - 5
       raket_AI.sety(y)

# GoalReset
def reset():
   bola.dx = random.choice([-1, 1])
   bola.dy = random.choice([-.65, .65])
   bola.color("blue")

# Call Key
SCREEN.listen()
SCREEN.onkeypress(raket_player_up, "Up")
SCREEN.onkeypress(raket_player_down, "Down")

while True:
   SCREEN.update()

   bola.setx(bola.xcor() + bola.dx)
   bola.sety(bola.ycor() + bola.dy)

   # TOPBORDER
   if bola.ycor() > 280.5:
       bola.sety(280.5)
       bola.dy *= -1
   # BOTBORDER
   if bola.ycor() < -275.5:
       bola.sety(-275.5)
       bola.dy *= -1

   # Left Goal Point
   if bola.xcor() < -390.5:
       bola.goto(0, 0)
       bola.dx *= -1
       poin_ai += 1
       reset()
       left_bounce = 0
       right_bounce = 0
       AIpoind.write("AI SCORED!", align="center", font=("Constantia", 15, "normal"))
       title.clear()
       title.write("Player: {}                                                 AI: {}       "
                   .format(poin_player, poin_ai), align="center", font=("Constantia", 24, "normal"))
   # Right Goal Point
   if bola.xcor() > 390.5:
       bola.goto(0, 0)
       bola.dx *= -1
       poin_player += 1
       reset()
       left_bounce = 0
       right_bounce = 0
       Ppoind.write("YOU SCORED!", align="center", font=("Constantia", 15, "normal"))
       title.clear()
       title.write("Player: {}                                                 AI: {}       "
                   .format(poin_player, poin_ai), align="center", font=("Constantia", 24, "normal"))

   # Raket Pantul
   if  (bola.ycor() < raket_AI.ycor() + 55.5 and bola.ycor() > raket_AI.ycor() - 55.5) and \
           (bola.xcor() > 340.5 and bola.xcor() < 350.5):
       bola.setx(340.5)
       bola.dx *= -1
       right_bounce += 1
       AIpoind.clear()

   if (bola.ycor() < raket_player.ycor() + 55.5 and bola.ycor() > raket_player.ycor() - 55.5) and \
           (bola.xcor() < -340.5 and bola.xcor() > -350.5):
       bola.setx(-340.5)
       bola.dx *= -1
       left_bounce += 1
       Ppoind.clear()

       if (left_bounce == right_bounce) and \
               (left_bounce > 2 and right_bounce > 2) and \
               (bola.dx <= 2 and bola.dy >= -2.45):
           bola.dx += .15
           bola.dy -= .15
           bola.color("red")

   # Ai Mover
   if raket_AI.ycor() < bola.ycor() and abs(raket_AI.ycor() - bola.ycor()) > 20.5:
       raket_AI_up()
   elif raket_AI.ycor() > bola.ycor() and abs(raket_AI.ycor() - bola.ycor()) > 20.5:
       raket_AI_down()
