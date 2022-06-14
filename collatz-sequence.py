# Collatz Sequence script
import time
import sys


def collatzOperation(number):  # performs collatz evaluation and returns number
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


def collatzLoop():  # handles user input and loops through a full collatz sequence
    count = 0  # keeps track of how many collatz iterations have passed
    while True:
        userNum = input('Enter an integer: ')
        userNumOriginal = userNum
        try:
            userNum = int(userNum)
            break
        except ValueError:
            print('Input must be an integer.')
            continue
    while userNum != 1:
        userNum = collatzOperation(userNum)
        print(userNum)
        count += 1
        time.sleep(0.2)  # artificial delay
    print('It took', count, 'iterations for the number you entered (' + userNumOriginal + ') to reach 1.')


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
