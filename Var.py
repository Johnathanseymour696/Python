#how to change a string into a list
myString = "Arizona"
mysteryWord = list(myString)
print(mysteryWord)
guessList = []
#How to make a list with_for characters

for letter in mysteryWord:
	guessList.append("_")

print(guessList)

#How to replace a specific index in a list 
guessList[3] = "z"

print(guessList)

