# Guessing Number Game with Nested Loop

secretnumber = 6
lowestNumber = 0
highestNumber = 10
guessCount = 0
guessLimit = 3


while guessCount < guessLimit:
    inputNumber = int(
        input(f"Select A Number Between {lowestNumber} to {highestNumber}: "))

    if inputNumber == secretnumber:
        print("You Won The Guessing Game...!!")
        break

    elif inputNumber <= lowestNumber:
        print(
            f"input number must not be lower than or equal to {lowestNumber}")
        guessCount = guessCount + 1

    elif inputNumber >= highestNumber:
        print(
            f"Your input number must not be higher than or equal to {highestNumber}")
        guessCount = guessCount + 1

    elif inputNumber < secretnumber:
        print("Your input number is too low")
        guessCount = guessCount + 1

    elif inputNumber > secretnumber:
        print("Your input number is too high")
        guessCount = guessCount + 1
else:
    print("Your Total Counts Has Been Finished.. Try Again")
