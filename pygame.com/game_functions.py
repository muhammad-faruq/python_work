import pygame
from car import Car

WHITE = (255, 255, 255)
GREEN = (38, 116, 64)
RED = (255, 0, 0)
GREY = (200, 200, 200)
PURPLE = (130, 0, 130)

def make_enemies():
	enemyCar = Car(PURPLE, 20, 30, randint(5,10))
	enemyCar.rect.x = randint(0, 400)
	enemyCar.rect.y = 0
	incoming_cars.add(enemyCar)
	
