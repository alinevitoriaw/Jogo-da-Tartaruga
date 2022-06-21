import turtle
import random

#primeira janela
janela = turtle.Screen()
janela.title("Turtle Game")
janela.bgcolor("orange")
janela.setup(width=600, height=600)
janela.tracer(0)

#segunda janela
janel2 = turtle.Turtle()
janel2.speed(10)
janel2.penup()
janel2.goto(-255, 255)
janel2.pendown()
janel2.hideturtle()
janel2.fillcolor("lightblue")
janel2.begin_fill()
janel2.pensize(2)

for i in range(4):
    janel2.forward(510)
    janel2.left(-90)
janel2.end_fill()

#tartaruga
tata = turtle.Turtle()
tata.shape("turtle")
tata.color("black")
tata.shapesize(1.5)
tata.penup()

#posição da maçã
maça = turtle.Turtle()
maça.shape("circle")
maça.color("red")
maça.penup()
maça.speed(0)
maça.setx(random.randrange(-255, 255))
maça.sety(random.randrange(-255, 255))
maça.distance(tata)
print(maça.distance(tata))

#posição do veneno
veneno = turtle.Turtle()
veneno.shape("circle")
veneno.color("green")
veneno.penup()
veneno.speed(0)
veneno.setx(random.randrange(-255, 255))
veneno.sety(random.randrange(-255, 255))
veneno.distance(tata)
print(veneno.distance(tata))

#movimentação
def movup():
    tata.forward(15)
def movleft():
    tata.left(15)
def movright():
    tata.right(15)
def movback():
    tata.back(15)

janela.listen()
janela.onkeypress(movup, "Up")
janela.onkeypress(movleft, "Left")
janela.onkeypress(movright, "Right")
janela.onkeypress(movback, "Down")

#criando a variavel para a pontuação
pontos = 0
vidas = 3
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("pontos: 0  vidas: 3", align="center", font=("Courier", 15, "normal"))

while True:
    janela.update()
    if tata.ycor() > 255 or tata.ycor() < -255:
        tata.right(90)
    if tata.xcor() > 255 or tata.xcor() < -255:
        tata.right(90)

    if tata.distance(maça) < 15:
        x = random.randint(-255, 255)
        y = random.randint(-255, 255)
        maça.goto(x, y)
    if tata.distance(veneno) < 15:
        x = random.randint(-255, 255)
        y = random.randint(-255, 255)
        veneno.goto(x, y)

janela.mainloop()