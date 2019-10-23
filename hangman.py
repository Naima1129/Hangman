import random
from random import choice

hi= input("What is your name? ")
print("Ok " + hi +", let's play hangman!")



myWord = choice(["dogs","fish","rocks"])
myList = list(myWord)

choice = input(" Type a word: ")

if choice == myWord:
	print("It's a match")
	print (" You have obtained victory!")
	
else:
	print("Sorry, that word isn't it ")

guessedLetters =[]
correctLetters= []


for a in myList:
	correctLetters.append("_")
print(correctLetters)

#how to check if a letter is in a word
play = True


while play:
	if correctLetters == myList:
		print("Congratulations, you got the word! ")
		break
	letter = input(" Type a letter ")

	if letter in myWord:
		print("Letter is in the word")
	
		if myWord == "dogs":
			if letter == "d":
				correctLetters[0] = "d"
			if letter == "o":
				correctLetters[1] = "o"
			if letter == "g":
				correctLetters[2] = "g"
			if letter == "s":
				correctLetters[3] = "s"
		elif myWord == "fish":
			if letter == "f":
				correctLetters[0]="f"
			if letter == "i":
				correctLetters[1]="i"
			if letter == "s":
				correctLetters[2]="s"
			if letter == "h":
				correctLetters[3]="h"

		else:
			if letter == "r":
				correctLetters[0]="r"
			if letter == "o":
				correctLetters[1]="o"
			if letter == "c":
				correctLetters[2]="c"
			if letter == "k":
				correctLetters[3]="k"
			if letter == "s":
				correctletters[4]="s"
		


			print(correctLetters)
			print("Guessed letters: " +str(guessedLetters))

			
	

	else:
		print("Letter is not in the word")
		guessedLetters.append(letter)
		print("Guessed letters: " +str(guessedLetters))




