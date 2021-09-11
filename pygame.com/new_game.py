import pygame
from car import Car
pygame.init()
import game_functions as gf

WHITE = (255, 255, 255)
GREEN = (38, 116, 64)
RED = (255, 0, 0)
GREY = (200, 200, 200)
PURPLE = (130, 0, 130)


size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")

cars = pygame.sprite.Group()

playerCar = Car()
playerCar.rect.x = 200
playerCar.rect.y = 300
cars.add(playerCar)

incoming_cars = pygame.sprite.Group()
# ~ enemyCar1 = Car(PURPLE, 20, 30, 10)
# ~ enemyCar2 = Car ()
# ~ enemyCar3

carryOn = True 
clock = pygame.time.Clock()

while carryOn:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			carryOn = False 
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		playerCar.moveLeft(5)
	if keys[pygame.K_RIGHT]:
		playerCar.moveRight(5)
	if keys[pygame.K_UP]:
		playerCar.moveUp(5)
	if keys[pygame.K_DOWN]:
		playerCar.moveDown(5)
	
	# Check for car collisions
	# ~ car_collision_list = pygame.sprite.spritecollide(playerCar, incoming_cars, False)
	# ~ for car in car_collision_list:
		# ~ print("Car Crash!")
		# ~ # End of Game
		# ~ carryOn = False
	
	# Game logic here
	cars.update()
	
	# Drawing background
	screen.fill(GREEN)
	pygame.draw.rect(screen, GREY, [40, 0, 200, 300])
	pygame.draw.line(screen, WHITE, [140, 0], [140, 300], 5)
	
	# Drawing cars
	cars.draw(screen)
	
	# Update the screen
	pygame.display.flip()
	
	# Limit to 60 FPS
	clock.tick(60)
	
pygame.quit()
