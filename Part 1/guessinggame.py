import random

def get_integer(prompt):
    """
    Get an integer from standard Input (stdin).

    The function will continue looping and prompting
    the user until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the use enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


help(get_integer)

lowest = 1
highest = 100
answer = random.randint(lowest, highest)
#print(answer)   # TODO: Remove after testing

print("please guess a number between {} and {}: ".format(lowest, highest))
guess = get_integer(": ")

tries = 1
while guess != answer and guess <= 10 :

    while guess < answer:
        print("Guess higher or Enter 0 to quit: ")
        break

    while guess > answer:
        print("Guess lower or Enter 0 to quit: ")
        break
    guess = get_integer(": ")

    while guess == 0 or tries > 10:
        print("Game over the answer was {}.".format(answer))
        break
    tries += 1

while guess == answer and tries == 1:
    print("Well done! You guessed correctly!")
    break

while guess == answer and tries > 1:
    print("Well done! You guessed correctly in {} attempts.".format(tries))
    break


# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess != answer:
#         print("Sorry, you have not guessed correctly")
#     else:
#         print("Well done, you guessed it")




# if guess != answer:
#     if guess > answer:
#         print("Please guess loweer")
#     else: # guess must be smaller than answer
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guess it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guess it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("you got it first time")