from tkinter import *
from KeyListener import *

class Spaceship():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = 'Spacesheep'
        self.speedX = 0
        self.speedY = 0
        self.mass = 1000
        self.photo = PhotoImage(file="images/Spaceship_up.gif")

    def move(self, delta) :
        self.speedX = self.accelX*delta + getSpeedSpaceX() + getSpeedScrollX()
        self.speedY = self.accelY*delta + getSpeedSpaceY() + getSpeedScrollY()
        
        self.x = convMeterToPixel(self.speedX*delta) + self.x
        self.y = convMeterToPixel(self.speedY*delta) + self.y 

        #Permet de gérer l'affichage du vaisseau selon son sens de déplacement
        if getSpeedSpaceX() > 0:
            self.photo = PhotoImage(file="images/Spaceship_right.gif")
        elif getSpeedSpaceX() < 0:
            self.photo = PhotoImage(file="images/Spaceship_left.gif")
        if getSpeedSpaceY() > 0:
            self.photo = PhotoImage(file="images/Spaceship_down.gif")
        elif getSpeedSpaceY() < 0:
            self.photo = PhotoImage(file="images/Spaceship_up.gif")

    def attract(self, xObj, yObj, massObj, theta):
        #On néglige l'attraction du vaisseau
        return [0,0]
