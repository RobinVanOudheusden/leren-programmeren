repeat = True

#intro
while repeat == True:
    naam = input("Welkom bij deze game, mag ik uw naam?: \n")
    leeftijd = input("Mag ik uw leeftijd?: \n")

    if int(leeftijd) < 16:
        print("Het spijt me, "+naam+". Je bent te jong om deze game te spelen..")
        quit()
#aanval kant
    else:
        startGame = input("MOVE 1: Wil je aanvallen of verdedigen?: \n")

        if startGame == "aanvallen":
            print("\nJe viel de tegenstander aan en raakte! \nYour HP: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ \nEnemies HP: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♡ ♡ ♡")
            move2a = input("MOVE 2: Wil je aanvallen of verdedigen?: \n")

            if move2a == "aanvallen":
                print("\nJe viel je tegenstander aan, maar hij verdedigde! Nu viel hij terug aan en raakte. \nYour HP: ♥ ♥ ♥ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♡ ♡ ♡")
                move3a = input("MOVE 3: Wil je aanvallen of verdedigen?: \n")

                if move3a == "verdedigen":
                    print("\nJe ontweek de aanval van je tegenstander met succes en kon daarbij terug aanvallen. CRITICAL HIT! \nYour HP: ♥ ♥ ♥ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
                    opnieuwspelen = input("Dit is het einde van de game, je hebt gewonnen! Wil je stoppen met spelen of nog een keer proberen? (quit/restart)\n").lower()

                    if opnieuwspelen == "quit":
                        print("Je hebt gekozen om te stoppen, totziens!")
                        quit()
                    
                    elif opnieuwspelen == "restart":
                        repeat = True

                if move3a == "aanvallen":
                    repeat = False
                    print("\nZowel jij als je tegenstander kozen voor aanvallen. Jullie vielen elkaar aan, maar je verloor.. \nYour HP: ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♥ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
                    opnieuwspelen = input("Dit is het einde van de game, je hebt verloren. Wil je stoppen met spelen of nog een keer proberen? (quit/restart)\n").lower()

                    if opnieuwspelen == "quit":
                        print("Je hebt gekozen om te stoppen, totziens!")
                        quit()
                    
                    elif opnieuwspelen == "restart":
                        repeat = True

            if move2a == "verdedigen":
                print("\nJe verdedigde de aanval van de tegenstander zonder succes, je bent geraakt! \nYour HP: ♥ ♥ ♥ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♡ ♡ ♡")
                move3a = input("MOVE 3: Wil je aanvallen of verdedigen?: \n")

                if move3a == "verdedigen":
                    print("\nJe verdediging loopt uit op groot succes! De tegenstander valt aan, maar struikelt, je weet hem de genadeklap te geven en gaat er vandoor met de overwinning! \nYour HP: ♥ ♥ ♥ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
                    opnieuwspelen = input("Dit is het einde van de game, je hebt gewonnen! Wil je stoppen met spelen of nog een keer proberen? (quit/restart)\n").lower()

                    if opnieuwspelen == "quit":
                        print("Je hebt gekozen om te stoppen, totziens!")
                        quit()
                    
                    elif opnieuwspelen == "restart":
                        repeat = True
                        
                if move3a == "aanvallen":
                    print("\nJe koos voor aanvallen, maar het was een domme zet. Je tegenstander verdedigde en viel terug aan. GAME over..... \nYour HP: ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♡ ♡ ♡")         
                    opnieuwspelen = input("Dit is het einde van de game, je hebt verloren. Wil je stoppen met spelen of nog een keer proberen? (quit/restart)\n").lower()

                    if opnieuwspelen == "quit":
                        print("Je hebt gekozen om te stoppen, totziens!")
                        quit()
                    
                    elif opnieuwspelen == "restart":
                        repeat = True      

#defend kant
        if startGame == "verdedigen":
            print("\nJe tegenstander viel aan, maar je verdedigde de aanval en kon terug aanvallen! \nYour HP: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ \nEnemies HP: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♡ ♡ ♡")
            move2b = input("MOVE 2: Wil je aanvallen of verdedigen?: \n")

            if move2b == "verdedigen":
                print("\nJe tegenstander viel aan, maar jij verdedigde. Je kreeg de kans om terug aan te vallen en raakte! \nYour HP: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ \nEnemies HP: ♥ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
                move3b = input("MOVE 3: Wil je aanvallen of verdedigen?: \n")

                if move3b == "aanvallen":
                    print("\nZowel jij als je tegenstander kiezen om aan te vallen, je tegenstander raakt een critical hit! Toch win je... op het nippertje! \nYour HP: ♥ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
                    opnieuwspelen = input("Dit is het einde van de game, je hebt gewonnen! Wil je stoppen met spelen of nog een keer proberen? (quit/restart)\n").lower()

                    if opnieuwspelen == "quit":
                        print("Je hebt gekozen om te stoppen, totziens!")
                        quit()
                    
                    elif opnieuwspelen == "restart":
                        repeat = True

                if move3b == "verdedigen":
                    print("\nJe koos voor verdedigen, maar de verdediging faalde en je tegenstander raakt je met een fatale hit. GAME OVER!!! \nYour HP: ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♥ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
                    opnieuwspelen = input("Dit is het einde van de game, je hebt verloren. Wil je stoppen met spelen of nog een keer proberen? (quit/restart)\n").lower()

                    if opnieuwspelen == "quit":
                        print("Je hebt gekozen om te stoppen, totziens!")
                        quit()
                    
                    elif opnieuwspelen == "restart":
                        repeat = True
            
            if move2b == "aanvallen":
                print("\nJe tegenstander slaagt in een critical hit. Zowel jij als je tegenstander lopen letsel op. \nYour HP: ♥ ♥ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♥ ♥ ♥ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
                move3b = input("MOVE 3: Wil je aanvallen of verdedigen?: \n")

                if move3b == "verdedigen":
                    print("\nJe koos voor verdedigen, maar je verdediging had geen effect en je tegenstander viel je aan. Verloren.. \nYour HP: ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♥ ♥ ♥ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
                    opnieuwspelen = input("Dit is het einde van de game, je hebt verloren. Wil je stoppen met spelen of nog een keer proberen? (quit/restart)\n").lower()

                    if opnieuwspelen == "quit":
                        print("Je hebt gekozen om te stoppen, totziens!")
                        quit()
                    
                    elif opnieuwspelen == "restart":
                        repeat = True

                if move3b == "aanvallen":
                    print("\nJe koos voor aanvallen, de verdediging van je tegenstander faalde en je maakte een fatale hit! \nYour HP: ♥ ♥ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ \nEnemies HP: ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
                    opnieuwspelen = input("Dit is het einde van de game, je hebt gewonnen! Wil je stoppen met spelen of nog een keer proberen? (quit/restart)\n").lower()

                    if opnieuwspelen == "quit":
                        print("Je hebt gekozen om te stoppen, totziens!")
                        quit()
                    
                    elif opnieuwspelen == "restart":
                        repeat = True