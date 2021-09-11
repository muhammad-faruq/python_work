import pygame
WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):
	# This car is a sprite
	
	def __init__(self):
		# Hello parents
		super().__init__()
		
		# Pass the color and its position. set background as transparent
		# ~ self.image = pygame.Surface([width, height])
		# ~ self.image.fill(WHITE)
		# ~ self.image.set_colorkey(WHITE)
		self.image = pygame.image.load("images/enemy.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (200, 150))
		# Initialize the attributes of car
		
		# Draw the car. its a rectangle

		
		#Instead we could load a proper picture of a car..
		
		
		# Fetch the rectagle cordinates of car
		self.rect = self.image.get_rect()
		
	def moveRight(self, pixels):
		if self.rect.right > 400:
			return None
		else:
			self.rect.x += pixels
		
	def moveLeft(self, pixels):
		if self.rect.left < 0:
			return None
		else:
			self.rect.x -= pixels
	
	def moveUp(self, pixels):
		if self.rect.top > 0:	
			self.rect.y -= pixels
	
	def moveDown(self, pixels):
		if self.rect.bottom < 500:
			self.rect.y += pixels
			
	def changeSpeed(self, speed):
		self.speed = speed
		
	def repaint(self, color):
		self.color = color
		pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
