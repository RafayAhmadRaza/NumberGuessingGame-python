import random



guess = 1
NumOfDigit = 3



MaxGuesses = 10


def secretNumber():
    sNumber = ''
    numberString = list('0123456789')
    random.shuffle(numberString)
    for i in range(NumOfDigit):
       sNumber+=str(numberString[i])
    
    return sNumber

def getClues(guessN,sNumber):
    if guessN == sNumber:
        return 'You Got IT!'
    clues = []

    for i in range(len(guessN)):
        if guessN[i] == sNumber[i]:
            clues.append('Fermi')
        elif guessN[i] in sNumber:
            clues.append('Pico')
    if len(clues)== 0:
        clues.append('Bagels')
    
    return " ".join(clues)

print("Bagels Game By Rafay Ahmad Raza\n From The Big Book of small PythonProjects")

print(f"I am thinking of a {NumOfDigit}-digit number. Please try to guess what it is\n Here are some clues:")

print("When I say:\tThat Means:")

print('Pico\tOne digit is correct but in the wrong position.\nFermi\tOne digit is correct and in the right position.\nBagels\tNo digit is correct.\nFor example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.\nI have thought up a number.')

SecretNumber = secretNumber()
print(f'You have {MaxGuesses} guesses')
while  True:

    while guess <= MaxGuesses:
        print(f'{guess} Guess Number')

        GuessNumber = input("Enter your guess: ")
        while len(GuessNumber) != NumOfDigit or not GuessNumber.isdecimal():
            print(f'{guess} Guess Number')
            GuessNumber = input('> ')
        
        clues = getClues(GuessNumber,SecretNumber)
        print(clues)
        guess +=1

        if GuessNumber == SecretNumber:
            break
        if guess>MaxGuesses:
            print("You have run out of guesses")
            print(f"the answer was {SecretNumber}")
        
    play = input("Do you want to play again: ")

    if play == 'n':
        print('Thank you for playing, take care :)')
        break
    else:
        guess=1
        SecretNumber=secretNumber()
