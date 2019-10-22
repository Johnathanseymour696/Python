#Johnathan Seymour
#P1
#make a variable to hold your list
todolist = []
print("Welcome to To Do List ")
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list ")
	print("Enter q to quit")
	choice = input("Choose:")

	if choice == "q":
		break
	elif choice == "a":
		add = input("What would you like to add?")
		todolist.append(add)
	elif choice == "r":
		#remove an item from the list
		todolist.remove(input("What would you like to remove?"))
	elif choice == "p":
		print(todolist)
		pass
	else:
		print("You choose something that was not listed.")