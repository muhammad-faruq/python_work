from random import randint
## Rock Paper Scissors Game
msg = 'Rock = 1\n'
msg += 'Paper = 2\n'
msg += 'Scissors = 3'

print("Would you like to play Rock Paper Scissors? ")
player_wins = 0
computer_wins = 0

def check_wins():
	global player_wins
	global computer_wins
	if win == 1:
		player_wins += 1
		computer_wins += 0
	if win == 2:
		player_wins += 0
		computer_wins += 1
	print("PLAYER SCORE: " + str(player_wins))
	print("COMPUTER SCORE: " + str(computer_wins))

start_game = input("(y/n) ")	

gameplay = True
autism = True
if start_game == 'y':
	print(msg)
	while autism:
		while gameplay:
			player_plays = input("\nChoose 1, 2 or 3: ")
			if player_plays == '1':
				print("Player: ROCK")
				choice = randint(1,3)
				if choice == 1:
					print("AI: ROCK")
				if choice == 2:
					print("AI: PAPER")
				if choice == 3:
					print("AI: SCISSORS")
				choices = str(choice)
				if choices == player_plays:
					print("\nIts a draw!")
					win = 0
				if choices == '1' and player_plays =='2':
					print("\nPAPER beats ROCK! You win!")
					win = True
				if choices == '2' and player_plays == '1':
					print("\nPAPER beats ROCK! You lose!")
					win = 2
				if choices == '1' and player_plays == '3':
					print("\nROCK beats SCISSORS! You lose!")
					win = 2
				if choices == '3' and player_plays == '1':
					print("\nROCK beats SCISSORS! You win!")
					win = 1
				if choices == '2' and player_plays == '3':
					print("\nSCISSORS beats PAPER! You win!")
					win = 1
				if choices == '3' and player_plays == '2':
					print("\nSCISSORS beats PAPER! You lose!")
					win = 2
				check_wins()
			
			if player_plays == '2':
				print("Player: PAPER")
				choice = randint(1,3)
				if choice == 1:
					print("AI: ROCK")
				if choice == 2:
					print("AI: PAPER")
				if choice == 3:
					print("AI: SCISSORS")
				choices = str(choice)
				if choices == player_plays:
					print("\nIts a draw!")
					win = 0
				if choices == '1' and player_plays =='2':
					print("\nPAPER beats ROCK! You win!")
					win = True
				if choices == '2' and player_plays == '1':
					print("\nPAPER beats ROCK! You lose!")
					win = 2
				if choices == '1' and player_plays == '3':
					print("\nROCK beats SCISSORS! You lose!")
					win = 2
				if choices == '3' and player_plays == '1':
					print("\nROCK beats SCISSORS! You win!")
					win = 1
				if choices == '2' and player_plays == '3':
					print("\nSCISSORS beats PAPER! You win!")
					win = 1
				if choices == '3' and player_plays == '2':
					print("\nSCISSORS beats PAPER! You lose!")
					win = 2
				check_wins()
				
			if player_plays == '3':
				print("Player: SCISSORS")
				choice = randint(1,3)
				if choice == 1:
					print("AI: ROCK")
				if choice == 2:
					print("AI: PAPER")
				if choice == 3:
					print("AI: SCISSORS")
				choices = str(choice)
				if choices == player_plays:
					print("\nIts a draw!")
					win = 0
				if choices == '1' and player_plays =='2':
					print("\nPAPER beats ROCK! You win!")
					win = True
				if choices == '2' and player_plays == '1':
					print("\nPAPER beats ROCK! You lose!")
					win = 2
				if choices == '1' and player_plays == '3':
					print("\nROCK beats SCISSORS! You lose!")
					win = 2
				if choices == '3' and player_plays == '1':
					print("\nROCK beats SCISSORS! You win!")
					win = 1
				if choices == '2' and player_plays == '3':
					print("\nSCISSORS beats PAPER! You win!")
					win = 1
				if choices == '3' and player_plays == '2':
					print("\nSCISSORS beats PAPER! You lose!")
					win = 2
				check_wins()
			if player_wins == 3:
				print("Congratulations, you have won the game!")
				gameplay = False
			if computer_wins == 3:
				print("Too bad, you have lost!")
				gameplay = False
		play_again = input("\nDo you want to play again??? (y/n) ")
		if play_again == 'y':
			gameplay = True
			player_wins = 0
			computer_wins = 0
		if play_again == 'n':
			break
print("Thank you for playing!")
			
			
