secretWord = "christmas"
secretWord = list(secretWord)
print(secretWord)
misses = 0 
hangman = ["first pic" , "Second pictur"]


guess = input("Guess a letter:")

if guess in secretWord:
	print("letter in secretWord")
else:
	misses = misses + 1

print("Misses: " + str(misses))
print(hangman[misses])