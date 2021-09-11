## Number guessing game
from random import randint

startGame = True
guessing = True
print("Welcome to Number Guesser!")
while startGame:
	start_game = input("Would you like to play? (y/n) ")
	generate_number = randint(0,100)
	if start_game == 'y':	
		print("Guess what number I am thinking!")	
		while guessing:
			player_guess = input("")
			if player_guess == str(generate_number):
				print("Congratulations, that is correct!")
				break
			elif int(player_guess) > generate_number:
				print("Too high! Try again!")
			elif int(player_guess) < generate_number:
				print("Too low! Try again!")
		
	elif start_game == 'n':
		print("Thanks for playing!")
		break
