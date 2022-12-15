import random
rondes = 20
punten = 0
ronde = 0

while ronde < rondes:
    getal = random.randint(0, 1000)
    print("Welkom bij 'RAAD HET GETAL'")
    print("In deze game ga je een getal raden tussen 1 en 1000.")
    print("Als je binnen een radius van 50 van het getal zit, krijg je de melding 'Je bent warm!' Zit je binnen een radius van 20 van het getal krijg je de melding 'Je bent heel warm!'")
    print("Het doel van de game is dat je zoveel mogelijk punten behaald binnen 20 rondes, succes!\n")

    pogingen = 10
    while pogingen > 0:
        geraden = int(input("Welk getal kies je?\n-------------------\n"))
        if geraden == getal:
            print("Gefeliciteerd! Je hebt het getal geraden.")
            punten += 1
            restart = input("Wil je door spelen? (y/n)\n")
            if restart == "y":
                break
            elif restart == "n":
                quit()

        elif geraden <= getal:
            print("Hoger!")
        elif geraden >= getal:
            print("Lager!")

        if (abs(getal - geraden)) <= 20:
            print("Je bent HEEL warm!")
        elif (abs(getal - geraden)) <= 50:
            print("Je bent warm!")

        ronde += 1
        print(f"Ronde: {ronde}")

        print(f"Punten: {punten}")

        pogingen -= 1
        print(f"Pogingen over: {pogingen}")

        if ronde == 10: 
            ronde10 = input("U heeft nu 10 rondes gehad. Wilt u nog verder? (y/n)\n")
            if ronde10 == "n":
                exit()
        if ronde == rondes:
            print(f"Je heb nu 20 rondes gespeeld. je totale score is: {punten}")