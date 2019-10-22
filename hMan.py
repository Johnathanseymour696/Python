import random
import os 
import sys
import time
print("Welcome to hangman")
print("For easy game press e")
print("For hard game press h")
print("To quit press q")
menu = input("What would you like to do?")

if menu == "e":
	List = [
     "cat","pony","zebra","kangaroo"
	]
	mysteryWord = random.choice(List)
	guess_word = []
	print(mysteryWord)
	for letter in mysteryWord:
		guess_word.append("_")
	print(guess_word)
	framelist = ['''
	|===
    |  |
	   |
	   |
	   |
	  ===
	''']

	guess = input('what letter would you like to put?')
	