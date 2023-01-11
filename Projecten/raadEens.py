import random
rondes = 0
punten = 0
pogingen = 0
repeat = True
MAX_POGINGEN = 10
MAX_RONDES = 5

print("\nWelkom bij 'RAAD HET GETAL'")
print("In deze game ga je een getal raden tussen 1 en 1000.")
print("Als je binnen een radius van 50 van het getal zit, krijg je de melding 'Je bent warm!' Zit je binnen een radius van 20 van het getal krijg je de melding 'Je bent heel warm!'")
print("Het doel van de game is dat je zoveel mogelijk punten behaald binnen 20 rondes, succes!\n")

while repeat == True:
    getal = random.randint(0, 1000)
    print(getal)
    repeat2 = True
    while repeat2 == True:    
        if pogingen == MAX_POGINGEN: 
            ronde10 = input("U heeft nu 10 pogingen gehad. Wilt u nog verder? (y/n)\n")
            if ronde10 == "y":
                pogingen = 0
                break
            elif ronde10 == "n":
                exit()
        elif rondes == MAX_RONDES:
            print(f"Je heb nu {MAX_RONDES} rondes gespeeld. je totale score is: {punten}")
            quit()
        
        geraden = int(input("Welk getal kies je?\n-------------------\n"))
        pogingen = pogingen + 1
        if geraden == getal:
            punten = punten + 1
            rondes = rondes + 1
            pogingen = 0
            print(f"Gefeliciteerd! Je hebt het getal geraden.\nPunten: {punten}")
            restart = input("Wil je door spelen? (y/n)\n")
            if restart == "y":
                repeat2 = False
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