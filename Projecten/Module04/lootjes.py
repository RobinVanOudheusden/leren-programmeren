import random

repeat = True
repeat2 = True
lijst = []

while repeat == True:
    naam = input("Geef (unieke) namen van spelers:\n").lower()

    if naam in lijst:
        print("Die naam zit al in de lijst.")
        continue

    else:
        lijst.append(naam)     
        if len(lijst) >= 3:
            repeat = False

while repeat2 == True:
    extra = input("Wil je nog extra namen toevoegen?: (y/n)\n")

    if extra == "y":
        toevoegen = input("Wie wil je nog meer toevoegen?:\n").lower()
        if toevoegen in lijst:  
            print("Die naam zit al in de lijst.")
            continue

        else:
            lijst.append(toevoegen)

    else:
        repeat2 = False
        random.shuffle(lijst)

        for index in range(len(lijst)-1):
            print(lijst[index],'heeft',lijst[index + 1])
        print(lijst[-1],'heeft',lijst[0])

