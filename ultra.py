import os
import pygame
import time
import random
import smbus
import time
from pygame.locals import *
import RPi.GPIO as GPIO

class pyscope :
 def __init__(self):
  "Ininitializes a new pygame screen using the framebuffer"

 def __del__(self):
  "Destructor to make sure pygame shuts down, etc."

pygame.init()
screen = pygame.display.set_mode((320, 240))
pygame.display.set_caption("Asistente de aparcamiento");
blanco = (158, 158, 158)
screen.fill(blanco)
foto = pygame.image.load('coche2.png').convert_alpha()
screen.blit(foto, (0, 0))
pygame.draw.line(screen,(0 ,0,0),(20,200),(300,200), 4)
pygame.draw.line(screen,(0 ,0,0),(50,180),(270,180), 5)
pygame.draw.line(screen,(0 ,0,0),(70,160),(250,160), 6)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
a=1
b=2
pygame.display.flip()

bus = smbus.SMBus(1)
address = 0x70

#SRF08 REQUIRES 5V

def write(value):
    bus.write_byte_data(address, 0, value)
    return -1

def lightlevel():
    light = bus.read_byte_data(address, 1)
    return light

def range():
    range1 = bus.read_byte_data(address, 2)
    range2 = bus.read_byte_data(address, 3)
    range3 = (range1 << 8) + range2
    return range3

while True:
    write(0x51)
    time.sleep(0.7)
    lightlvl = lightlevel()
    rng = range()
    print lightlvl
    print rng
	
    if rng<15:
		GPIO.output(7, GPIO.HIGH)
        screen.fill(blanco)
		font = pygame.font.Font(None,20)
		text = font.render(str(rng), True, (255,255,255), (158,158,158))
		foto = pygame.image.load('coche2.png').convert_alpha()	
		screen.blit(foto, (0, 0))	
		pygame.draw.line(screen,(0 ,0,0),(20,200),(300,200), 4)
        pygame.draw.line(screen,(0 ,0,0),(50,180),(270,180), 5)
        pygame.draw.line(screen,(255 ,0,0),(70,160),(250,160), 6)		
		if lightlvl>150:		
			foto2 = pygame.image.load('sun_icon.png').convert_alpha()
			screen.blit(foto2, (300, 220))		
		elif lightlvl<150:                
			foto2 = pygame.image.load('item_menu.png').convert_alpha()
			screen.blit(foto2, (300, 220))
			screen.blit(text, (10,220))
        pygame.display.flip()

    elif rng<30:
        screen.fill(blanco)
        font = pygame.font.Font(None,20)
        text = font.render(str(rng), True, (255,255,255), (158,158,158))
        if a==1:
           GPIO.output(7, GPIO.HIGH)
           a=0
        foto = pygame.image.load('coche2.png').convert_alpha()
        screen.blit(foto, (0, 0))
        pygame.draw.line(screen,(255 ,255,100),(50,180),(270,180), 5)
        pygame.draw.line(screen,(0 ,0,0),(20,200),(300,200), 4)
        pygame.draw.line(screen,(0 ,0,0),(70,160),(250,160), 6)
        GPIO.output(7, GPIO.LOW)
        a=a+1		
		if lightlvl>150:                
			foto2 = pygame.image.load('sun_icon.png').convert_alpha()
			screen.blit(foto2, (300, 220))
		elif lightlvl<150:               
			foto2 = pygame.image.load('item_menu.png').convert_alpha()
			screen.blit(foto2, (300, 220))
			screen.blit(text, (10,220))
		pygame.display.flip()

    elif rng<55:
		screen.fill(blanco)
        font = pygame.font.Font(None,20)
        text = font.render(str(rng), True, (255,255,255), (158,158,158))
        if b==2:
           GPIO.output(7, GPIO.HIGH)
           b=0
        foto = pygame.image.load('coche2.png').convert_alpha()
        screen.blit(foto, (0, 0))        
        pygame.draw.line(screen,(0 ,255,0),(20,200),(300,200), 4)
        pygame.draw.line(screen,(0 ,0,0),(50,180),(270,180), 5)
		pygame.draw.line(screen,(0 ,0,0),(70,160),(250,160), 6)
		GPIO.output(7, GPIO.LOW)
        b=b+1
		if lightlvl>150:
            foto2 = pygame.image.load('sun_icon.png').convert_alpha()
			screen.blit(foto2, (300, 220))
        elif lightlvl<150:               
			foto2 = pygame.image.load('item_menu.png').convert_alpha()
			screen.blit(foto2, (300, 220))
			screen.blit(text, (10,220))
        pygame.display.flip()
		
    else:
		GPIO.output(7, GPIO.LOW)	
       	screen.fill(blanco)
		foto = pygame.image.load('coche2.png').convert_alpha()
		screen.blit(foto, (0, 0))	
		pygame.draw.line(screen,(0 ,0,0),(20,200),(300,200), 4)
		pygame.draw.line(screen,(0 ,0,0),(70,160),(250,160), 6)
        pygame.draw.line(screen,(0 ,0,0),(50,180),(270,180), 5)
		if lightlvl>150:
            foto2 = pygame.image.load('sun_icon.png').convert_alpha()
			screen.blit(foto2, (300, 220))
		elif lightlvl<150:
            foto2 = pygame.image.load('item_menu.png').convert_alpha()
			screen.blit(foto2, (300, 220))
        pygame.display.flip()

    
