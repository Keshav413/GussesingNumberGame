import random
number = random.randint(1, 100)
print ("welcome to the game")
print ("please enter a number between 1 and 100 : ")
guess = int(input())
while True:
    if 1 > guess or guess > 100:
        print("number is not in range")
        break
    elif guess < number:
        print("you are lower side of the number")
    elif guess > number:
        print("you are higher side of the number")
    elif guess == number:
        print("congratulations! you guessed the number")
        break

    guess = int(input("enter new number : "))
