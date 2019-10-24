import random
from random import choice

hi= input("What is your name? ")
print("Ok " + hi +", let's play hangman!")

myWord = choice(["dogs","fish","rocks"])
myList = list(myWord)

correctLetters= []
guessedLetters =[]


for a in myList:
	correctLetters.append("_")
print(correctLetters)



missCount = input("How many misses are allowed? ")
print(missCount)


choice = input(" Type a word: ")
print(correctLetters)


if choice == myWord:
	print("you got the word")
	
else:
	print("Sorry, that word isn't it ")





misses= 0
if choice == myWord:
	print("It's a match")
	print (" You have obtained victory!")
else:

	while str(misses) < missCount:

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


				print(correctLetters)
				print("Guessed letters: " +str(guessedLetters))

			if myWord == "fish":
				if letter == "f":
					correctLetters[0]="f"
				if letter == "i":
					correctLetters[1]="i"
				if letter == "s":
					correctLetters[2]="s"
				if letter == "h":
					correctLetters[3]="h"


				print(correctLetters)
				print("Guessed letters: " +str(guessedLetters))

			if myWord== "rocks":
				if letter == "r":
					correctLetters[0]="r"
				if letter == "o":
					correctLetters[1]="o"
				if letter == "c":
					correctLetters[2]="c"
				if letter == "k":
					correctLetters[3]="k"
				if letter == "s":
					correctLetters = "s"
			


				print(correctLetters)
				print("Guessed letters: " +str(guessedLetters))

				
		

		else:
			print("Letter is not in the word")
			guessedLetters.append(letter)
			print("Guessed letters: " +str(guessedLetters))
			print(correctLetters)
			misses += 1
	print("Too many misses, Game over")






