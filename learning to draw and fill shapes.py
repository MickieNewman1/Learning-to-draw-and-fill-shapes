# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:37:53 2020

@author: mwnew
"""

#20/01/24


from turtle import *

window = Screen()

#create a screen and upload the bric wall picture 
window.screensize(400,600)
window.update()
window.bgpic('brick-wall.gif')

# make a green circle

greenCircle = Turtle()
greenCircle.color("#395B50")
greenCircle.width(5)
greenCircle.up()
greenCircle.backward(200)
greenCircle.down()
greenCircle.begin_fill()
greenCircle.circle(300, 360)
greenCircle.end_fill()

# make a light blue sircle within the green circle that is filled with a different shade of blue 
#
lightBlueInGreen = Turtle()
lightBlueInGreen.color("#92AFD7","#C5D1EB")
lightBlueInGreen.width(10)
lightBlueInGreen.up()
lightBlueInGreen.backward(200)
lightBlueInGreen.down()
lightBlueInGreen.begin_fill()
lightBlueInGreen.circle(100,360)
lightBlueInGreen.end_fill()

# make a blue star filled in with dark green 

blueStar = Turtle()
blueStar.color("#5A7684","#1F2F16")
blueStar.width(5)
blueStar.up()
blueStar.left(20)
blueStar.forward(200)
blueStar.down()
length= 300
turn = 180-25.714 # the angle for a seven pointed star
blueStar.begin_fill()
blueStar.forward(length)
blueStar.left(turn)
blueStar.forward(length)
blueStar.left(turn)
blueStar.forward(length)
blueStar.left(turn)
blueStar.forward(length)
blueStar.left(turn)
blueStar.forward(length)
blueStar.left(turn)
blueStar.forward(length)
blueStar.left(turn)
blueStar.forward(length)
blueStar.end_fill()

# going to play with some polygons 

#upon realizing I needed a discontinuous line I started to play with things and it looks pretty cool.
beautifulLine = Turtle()
beautifulLine.color("#92AFD7")
beautifulLine.width(30)
beautifulLine.down()
beautifulLine.forward(50)
beautifulLine.right(90)
beautifulLine.forward(50)
beautifulLine.right(90)
beautifulLine.forward(50)
beautifulLine.up()
beautifulLine.forward(50)
beautifulLine.down()
beautifulLine.forward(50)
















done()

