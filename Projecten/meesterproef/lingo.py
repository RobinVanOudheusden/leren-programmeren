import random
from lingoWords import words
from termcolor import colored

def get_random_word(words):
    return random.choice(words)

def get_first_letter(random_woord):
    eerste_letter = random_woord[0]
    return eerste_letter

while True:
    print('Welkom bij Lingo!')
    print("Voer een 5-letterwoord in en druk op Enter!\n")

    woord = get_random_word(words)
    eerste_letter = get_first_letter(woord)
    print("Het woord begint met de letter: " + eerste_letter)
    print(woord)

    opnieuw_spelen = ""

    for poging in range(1,6):
        while True:
            raad = input(f"Poging {poging}: ").lower()
            if len(raad) == 5:
                break
            else:
                print("Het woord moet 5 letters lang zijn!")

        correcte_letters = ""

        for i in range(5):
            if raad[i] == woord[i]:
                correcte_letters += colored(raad[i], 'green')
            elif raad[i] in woord:
                correcte_letters += colored(raad[i], 'yellow')
            elif raad[i] not in woord:
                correcte_letters += colored(raad[i], 'red')
            else:
                 correcte_letters += raad[i]

        print(correcte_letters)

        if raad == woord:
            print(colored(f"Gefeliciteerd! Je hebt het woord geraden in poging {poging}!", 'red'))
            break

        if poging == 5:
            print(colored(f"Helaas, je hebt het woord niet geraden. Het woord was '{woord}'.", 'red'))

    opnieuw_spelen = input("Wil je opnieuw spelen? Typ 'quit' om af te sluiten. Klik Enter om door te spelen.\n")
    if opnieuw_spelen.lower() == 'quit':
        break