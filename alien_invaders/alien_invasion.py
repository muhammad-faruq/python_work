import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf

def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Make play button.
	play_button = Button(ai_settings, screen, 'Play')
	
	# Create an instance to create and store game statistics.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	# Make a ship, group of bullets, group of aliens.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	# Create a fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# Start the main loop for the game.
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		
		if stats.game_active:	
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, 
			aliens, bullets, play_button)
		
run_game()

