import random
from random import choice

hi= input("What is your name? ")
print("Ok " + hi +", let's play hangman!")



myWord = choice(["dogs"])
myList = list(myWord)

choice = input(" Type a word: ")

if choice == myWord:
	print("It's a match")
	print (" You have obtained victory!")
else:
	print("Sorry, that word isn't it ")
guessedLetters =[]
correctLetters= []
word = []

for a in myList:
	correctLetters.append("_")
print(correctLetters)

#how to check if a letter is in a word
play = True

if word == "dogs":
	print("Congrats you won! ")
	break
while play:

	letter = input(" Type a letter ")

	if letter in myWord:
		print("Letter is in the word")
	
		if myWord == "dogs":
			if letter == "d":
				correctLetters[0] = "d"
				word.append("d")
			

			if letter == "o":
				correctLetters[1] = "o"
				word.append("o")


			if letter == "g":
				correctLetters[2] = "g"
				word.append("g")


			if letter == "s":
				correctLetters[3] = "s"
				word.append("s")

			print(correctLetters)

	

	else:
		print("Letter is not in the word")
		guessedLetters.append(letter)
		print("Guessed letters: " +str(guessedLetters))




