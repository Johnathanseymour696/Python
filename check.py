#This is a check/review to make sure nothing was "lost" over break

#Johnathan Seymour
#P1


#Variable declaration and assignment
#example
myVar = "hello"
# Try to , declare two variables 1 string and 1 a number, and assign values
myNum = 1 
#while loop
# Example
x = 11
while x > 0:
	print(x)
	x = x - 1
# you try, print your name 100 times
myNumber = 100
while myNumber > 0:
	print("Johnathan Seymour" + str(myNumber))
	myNumber = myNumber -1
#String concatenation
#Example
name = "Johnathan"
print("Hello " + name)
#make a variable with your favorite move
#print "My favorite movie is " and then the value stored in the variable
fmovie = "The Terminal"
print("My favorite movie is " + fmovie)

myName = input("What is your name :")
print("Your name is " + myName)
# prompt for favorite song and print your favorite song is: ""
song = input("What is you favorite song ? :")
print("Your favorite song is " + song)
# casting: Changing the type of variable
myMath = 40
print("My Number is " + str(myMath))
num1 = input("Enter a number: ")
num1 = int(num1) + 10
print("num1 + 10= "+ str(num1))

#ask for two numbers add them together and print the result
num2 = input("What is your first number ?: ")
num3 = input("What is your second number ?: ")
num4 = int(num2) + int(num3)
print("First number + Second number = " + str(num4))
#if/else
#example
num = int(input("Type a number: "))
if num > 100:
	print("Your number is more than 100")
elif num1 == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less then 100")
#ask if today is your birthday, if it is print happy birthday
birthday = input("Is it your birthday today (yes/no) ?")
if birthday == 