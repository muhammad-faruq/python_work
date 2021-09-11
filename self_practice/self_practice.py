import sys

import pygame

def update_screen(screen):
	screen.fill( 0, 0, 230)

def run_game():
	
	pygame.init()
	screen = pygame.display.set_mode((1300, 700))
	pygame.display.set_caption("Self Practice")
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				print(event.key)
			update_screen(screen)
				
		pygame.display.flip()
		
run_game()
