import random
import os 
import sys
import time
EwordList = [
"lion","cat","mouse","bat"
         ]
guess_word = []
cguess = random.choice(EwordList)#The computer picks the random options
lengthw = len(cguess)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letterS = []

def beginning():
	print("Welcome to hangman")

	while True:
		choice = input("Whould you like to play hangman")

		if choice == "yes":
			print("welcome to hangman")
		else:
			break
beginning()


def change():
	for character in secret:
		guess_word.append("_")
    print("Ok so they word you need to guess has", lengthw , "characters")

    print("Be aware that you can only enter one letter from a-z\n\n")

    print(guess_word)