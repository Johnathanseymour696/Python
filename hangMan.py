#Johnathan Seymour
#P1
#10/21/19
myWord = "hello"

choice = input("Type a word: ")

if choice == myWord:
	print("It's a match")
else: 
	print("Thats not a match")

# how to check if a letter is in a word 
letter = input("Enter a letter:")

if letter in myWord:
	print("That letter is in the word")
else:
	print("Letter is not in word")
myList = list(myWord)
count = 0
for letter2 in myList:
	if letter2 == letter:
		print (count)
	count += 1