import random
import os 
import sys
print("Welcome to hangman")
print("For easy game press e")
print("For hard game press h")
print("To quit press q")
menu = input("What would you like to do?")

if menu == "e":
	numLoose = input("")
	List = [
     "cat","dog","cow","bat"
	]
	guess_word = []
	Word = random.choice(wordlist)
	

elif menu == "h":
	break
elif menu == "q":
	break
else:
	print("That is not a correct input")
