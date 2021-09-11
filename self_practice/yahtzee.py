from random import randint

def rolling():	
	print("\nHere are your rolls: ")
	print(str(r_1) + "  " + str(r_2) + "  " + str(r_3) +
	"  " + str(r_4) + "  " + str(r_5) + '\n')
	
print("Let's play Yahtzee")
"""Rolling dice game. To win roll 5 for all 5 dice"""

"""Automatic Yahtzee!"""

begin_game = input("Would you like to start auto rolling? (y/n) ")
if begin_game == 'y':
	auto_roll = True
	number_of_rolls = 0
	while auto_roll:
		print("\nNo. of rolls: " + str(number_of_rolls))
		r_1 = randint(1,6)
		r_2 = randint(1,6)
		r_3 = randint(1,6)
		r_4 = randint(1,6)
		r_5 = randint(1,6)
		rolling()
		number_of_rolls += 1
		if r_1 == r_2 == r_3 == r_4 == r_5 == 5:
			print('\n========================================================')
			print("		Y A H T Z E E ! ! ! ! ! !")
			print('========================================================')
			print("\nIt took you " + str(number_of_rolls) + " rolls to win!")
			number_of_rolls = 0
			auto_roll = False
		else:
			continue
else:
	print("Thank you for playing!")


"""Manual Version"""

# ~ number_of_rolls = 0
# ~ while True:
	# ~ message = "To roll the dice, press [ENTER]."
	# ~ message += "If not, type 'quit'.  "
	# ~ want_to_roll = input(message)
	# ~ if want_to_roll == "":
		# ~ number_of_rolls += 1
		# ~ print("\nNo. of rolls: " + str(number_of_rolls))
		# ~ r_1 = randint(1,6)
		# ~ r_2 = randint(1,6)
		# ~ r_3 = randint(1,6)
		# ~ r_4 = randint(1,6)
		# ~ r_5 = randint(1,6)
		# ~ rolling()
		# ~ if r_1 == r_2 == r_3 == r_4 == r_5 == 5:
			# ~ print('\n===============================================')
			# ~ print("				Y A H T Z E E ! ! ! ! ! !")
			# ~ print('===============================================')
			# ~ print("\nIt took you " + str(number_of_rolls) + " to win!")
			# ~ print('\n')
			# ~ number_of_rolls = 0
		# ~ else:
			# ~ continue
	# ~ elif want_to_roll == 'quit':
		# ~ print("Thank you for playing!")
		# ~ break
	# ~ elif want_to_roll == 'roll count':
		# ~ print('\n===============================================')
		# ~ print("You have rolled a total of " + str(number_of_rolls) + " times.")
		# ~ print('===============================================')
