# Collatz Sequence
import time
import sys


def collatzOperation(number):  # performs collatz evaluation and returns number
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    print(number)
    return number


def collatzLoop():  # handles user input and loops through a full collatz sequence
    count = 0  # keeps track of how many collatz iterations have passed
    while True:
        userNum = input('Enter an integer: ')
        try:
            userNum = int(userNum)
            break
        except ValueError:
            print('Input must be an integer.')
            continue
    while userNum != 1:
        userNum = collatzOperation(userNum)
        count += 1
        time.sleep(0.2)  # artificial delay
    print('It took', count, 'iterations for the number you entered to reach 1.')


def main():  # handles branching user inputs
    print('This program will perform the Collatz Sequence on any integer that you enter.')
    while True:
        collatzLoop()
        while True:  # play again decision loop
            playAgain = input('Would you like to play again?\n1. Yes \n2. No\n')
            try:
                playAgain = int(playAgain)
                if playAgain == 2:
                    print('Thanks for playing.')
                    sys.exit()
                elif playAgain == 1:
                    break
                else:
                    print('Input must be "1" or "2"')
                    continue
            except ValueError:
                print('Input must be an integer.')
                continue


main()
