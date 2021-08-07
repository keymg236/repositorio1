#PASO 0
import turtle
#PASO 5
import time
from typing import Counter
posponer = 0.1

#PASO 8 COLIZCION
import random

#PASO 12
# marcador
score = 0
high_score = 0

import math


#PASO 1
# config. window
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("Black")
wn.setup(width = 600, height=600)
wn.tracer(0)

#PASO 2
#cabeza of snake
cabeza= turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("yellow")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"

#`PASO 7`
#COMIDA
comida= turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#PASO 9
#cuerpos de la sarpiente([segmentos]
segmentos=[]
#PARTE 12
# TEXTO MENU
texto= turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()# esconde o no aparecera la pluma
texto.hideturtle()
texto.goto(0,200)
texto.write("Score: 0       High Score: 0", align = "center", font = ("Courier",24, "normal"))





#PASO 6
#FUNCIONES de teclado
def arriba():
    cabeza.direction= "up"
def abajo():
    cabeza.direction="down"
def izquierda():
    cabeza.direction="left"
def derecha():
    cabeza.direction="right"




#PASO 4
#Ejes de movmiento funciones
def mov():
    if cabeza.direction=="up":
        y = cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction=="down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction=="left":
        x = cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction=="right":
        x = cabeza.xcor()
        cabeza.setx(x+20)
#PASO 7
#eventos de teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha,"Right")



#PASO 3
# Bucle principal Se actualiza constantemente
while True:
    wn.update()

    #PASO 10
    # config bordes colisiones 
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        #PASO 10
        #esconder los segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000) #.goto concepto ubicacion (ir a) 
        #PASO 10
        #limpiar lista de segmenteos
        segmentos.clear()
        
        #PASO 12
        # RESETEAR MARCADOR
        score = 0
        texto.clear()
        texto.write("Score: {}      High Score: {}".format(score,high_score),\
                align = "center", font = ("Courier",24, "normal"))
    
    #coalicion comidax #PASO 8
    if cabeza.distance(comida) < 20:#PASO 8 COLIZCION
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()#PASO 9 SEGMENTO
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #PASO 12
        score += 10

        if score > high_score:
            high_score = score
        
        texto.clear()
        texto.write("Score: {}      High Score: {}".format(score,high_score),\
                align = "center", font = ("Courier",24, "normal"))


        

    #PASO 9
    #MOVER EL CUERPO DE SNAKE
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)
    
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()##PASO 4

    #PARTE 11 COLISIONES CON EL CUERPO
    # colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction= "stop"

            #esconder esos segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
            
            segmentos.clear()
            # PASO 12
            # COLISION CON EL CUERPO RESETEAR MARCADOR
            score = 0
            texto.clear()
            texto.write("Score: {}      High Score: {}".format(score,high_score),\
                align = "center", font = ("Courier",24, "normal"))
    
    time.sleep(posponer)##PASO 5
            

# input("Press any key to exit ...")
