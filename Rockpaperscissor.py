									
	# Included all required modules namely __future__ , string , colorama , random & time
from __future__ import print_function    # use print-function from time
from string import upper                 # use upper function from string
from colorama import Fore                # use Fore function from colorama
import random
from time import sleep                   # use sleep function from time

# Define function RPSgame for executing all functions of the game, Rock,Paper & Scissor

def RPSgame():

# Define lists for further usage in the code

	list = ['Paper','Scissor','Rock']
	list1 = ['Scissor', 'Paper']
	list2 = ['Rock', 'Scissor']
	list3 = ['Paper', 'Rock']
	group = [list1, list2, list3]


# Choose one of the modes from Player vs Computer and Computer vs Computer

	print(Fore.MAGENTA+'Choose mode:')
	print (Fore.BLACK+'       1. Player vs Computer')
	print ('       2. Computer vs Computer \n')

	mode = int(input(Fore.MAGENTA+"Enter: "+Fore.BLACK+ "'1' or '2' - "))   # Press integer 1 or 2 where 1: Player vs Computer and 2: Computer vs Computer

# If user enters mode is 1

	if mode == 1:

		while True:
			print (Fore.RED +' PLEASE WAIT ! GAME LOADING '.rjust(90), end='')    # Implementation of a pattern  before game loads
			sleep(0.4)
			for x in range(5):
				print('.', end='')
				sleep(0.4)
# Instructions to be read before the choice is entered

 			print(Fore.MAGENTA+'\nINSTRUCTIONS :-')
			print(Fore.BLACK+'            1. First letter should be upper case')
			print('            2. No space before entering your choice')
			print('            3. Press enter after entering your choice \n')

# User inputs a choice from Rock,Paper or Scissor stored in choice1
			choice1 = raw_input(Fore.MAGENTA+"Enter: " + Fore.BLACK + "Rock, Paper or Scissor ? ")

# Check if the user's input is valid , if not prompt to reenter

			while choice1 not in list:
				print(Fore.MAGENTA+'\nINCORRECT INPUT!FOLLOW INSTRUCTIONS:-')
				print (Fore.BLACK+'                                  1. First letter should be upper case')
				print ('                                  2. No space before entering your choice')
				print ('                                  3. Press enter after entering your choice\n')
				choice1 = raw_input(Fore.MAGENTA+"Enter: "+ Fore.BLACK+'Rock, Paper or Scissor ? ')
				print('\n')

# Computer's choice stored in choice2

			choice2 = random.choice(list)

# Store the inputs of player & computer as list

			choice = [choice1,choice2]
			choicerev = choice[::-1]

# Identify who wins , Player or Computer?

			for i in group:

# Compare the inputs of the players(choicerev/choice) with the whole list defined (group) above

				if choicerev==i:
					print(Fore.BLUE + 'Your choice - '.rjust(80), end ='' + Fore.BLACK + (choice1) + '\n')
					print (Fore.BLUE + 'Computer\'s choice - '.rjust(80), end='' + Fore.BLACK+upper(choice2)+'\n')
					sleep(0.4)
					print (Fore.RED+"YOU LOSE!".center(145))
				elif choice==i:
					print (Fore.BLUE+'Your choice - ' .rjust(80), end ='' + Fore.BLACK+upper(choice1) + '\n')
					print (Fore.BLUE+'Computer\'s choice - '.rjust(80), end=''  + Fore.BLACK+upper(choice2)+'\n')
					sleep(0.4)
					print (Fore.RED+"YOU WIN!".center(145))
			if choice1==choice2:
				print(Fore.BLUE+'Your choice - '.rjust(80), end ='' + Fore.BLACK+upper(choice1) + '\n')
				print (Fore.BLUE+'Computer\'s choice - ' .rjust(80), end ='' + Fore.BLACK+upper(choice2)+'\n')
				sleep(0.4)
				print (Fore.RED+"TIE".center(145))

# Ask player if the game needs to be continued , change the mode or end the game

			print(Fore.MAGENTA+'Choose one: ')
			print (Fore.BLACK +'1.Play again')
			print ('2.Change mode')
			print ('3.Any other number to end game \n')
			userch = int(input(Fore.MAGENTA+'Enter: '+Fore.BLACK+"'1' or '2' or 'any number? ':  "))
			if userch == 1:  # Play again
				continue
			elif userch == 2: # Change mode of play
				RPSgame()
			else: # any other number means game ends
				print ('\n\n\n')
				print(Fore.RED + '  GAME ENDS  '.center(160,'*'))
				exit()

# Computer vs Computer

	elif mode == 2:
		while True:
			group1 = ['Paper','Scissor','Rock']
			group2 = ['Scissor','Rock','Paper']

# Implementation of a pattern before game loads

			print (Fore.RED + ' PLEASE WAIT ! GAME BEGINS '.rjust(90),end='')
			sleep(0.4)
			for x in range(5):
				print('.', end='')
				sleep(0.4)
			print('\n')

# Generate the choices of the computers and store in choice3 and choice4

			choice3 = random.choice(group1)
			choice4 = random.choice(group2)

			choice = [choice3, choice4]
			choicerev = choice[::-1]

#Find who wins the game

			for i in group:
# Compare the inputs of the players(choicerev/choice) with the whole list defined (group) above
				if choicerev == i:
					print(Fore.BLUE+'Player1:- '.rjust(78), end ='' + Fore.BLACK+upper(choice3)+'\n')
					print (Fore.BLUE+'Player2:- ' .rjust(78), end ='' + Fore.BLACK+upper(choice4) +'\n')
					sleep(0.4)
					print(Fore.RED+"PLAYER 2 WINS!".center(151))
				elif choice == i:
					print(Fore.BLUE+'Player1:- '.rjust(78), end ='' + Fore.BLACK+ upper(choice3) + '\n')
					print (Fore.BLUE+'Player2:- '.rjust(78), end ='' + Fore.BLACK+upper(choice4) + '\n')
					sleep(0.4)
					print(Fore.RED+"PLAYER 1 WINS !".center(151))
			if choice3 == choice4:
				print(Fore.BLUE+'Player1:- '.rjust(78), end ='' + Fore.BLACK+upper(choice3) + '\n')
				print(Fore.BLUE+'Player2:- '.rjust(78), end ='' +  Fore.BLACK+upper(choice4) + '\n')
				sleep(0.4)
				print(Fore.RED+"TIE".center(151))

#Ask the user to continue the game, change the mode or end the game

			print(Fore.MAGENTA + 'Choose one: ')
			print(Fore.BLACK + '1.Play again')
			print('2.Change mode')
			print('3.Any other number to end game \n')
			userch = int(input(Fore.MAGENTA + 'Enter: ' + Fore.BLACK + "'1' or '2'or 'any number': "))

			if userch == 1:  # Play again
				continue
			elif userch == 2: # Change mode of play
				RPSgame()
			else:  # any other integer input means game ends
				print('\n\n\n')
				print(Fore.RED + ' Game Ends '.center(150, '*'))
				exit()

# If user inputs any other input than 1 or 2

	else:

		print(Fore.RED + 'INVALID INPUT'.center(150))
		flag = int(input(Fore.BLACK+"Do you want to continue? Enter 1 for YES and 2 for NO"))

# If user enters Y the game begins again or exit out of the code

		if flag==1:
			RPSgame()
		else:
			exit()


# call the function

RPSgame()
									
								
									
