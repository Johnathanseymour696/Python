countDown = input("What number would you like to countdown from")
while (countDown >= 0):
    if countDown != 0:
        print(countDown)
        countDown = countDown - 1
    else:
        print("Action!")
        break
