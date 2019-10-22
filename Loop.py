import random
#Johnathan Seymour
#dice Simulator
#P1 10/4/19

print("Dice Simulator")
numRolls = str(input("How many rolls?"))
x=1
while x<=numRolls:
	randomNum= random.randint(1,6)
	print("Dice rolled a :" + randomNum)
	x+=1