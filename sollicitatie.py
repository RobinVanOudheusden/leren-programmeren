punten = 0

vraag_naam = input("Hallo! Welkom bij dit sollicitatiegesprek, wat is uw naam?\n")

gefaald = ("\nHelaas " + vraag_naam + ", wij hebben geconstanteerd dat u niet aan de benodigde eisen van deze baan voldoet. :(")

vraag1 = input("\nHoeveel jaar ervaring heeft u met dieren?\n")
if float(vraag1) > 4:
    punten = punten + 1

vraag2 = input("\nHoeveel jaar ervaring heeft u met dressuur?\n")
if float(vraag2) > 4:
    punten = punten + 1

vraag3 = input("\nHoeveel jaar ervaring heeft u met jongleren?\n")
if float(vraag3) > 5:
    punten = punten + 1

vraag4 = input("\nHoeveel jaar ervaring heeft u met acrobatiek?\n")
if float(vraag4) > 3:
    punten = punten + 1

vraag5 = input("\nHeeft u een mbo-4 diploma of hoger? (y/n)\n")
if (vraag5) == "y":
    punten = punten + 1

vraag6 = input("\nBent u in bezit van een geldig Vrachtwagen rijbewijs? (y/n)\n")
if (vraag6) == "y":
    punten = punten + 1

vraag7 = input("\nBent u in bezit van een hoge hoed? (y/n)\n")
if (vraag7) == "y":
    punten = punten + 1

vraag8 = input("\nWat voor geslacht bent u?\n 1. man \n 2. vrouw\n\n")
if float(vraag8) == 1:
    vraag8a = input("\nHeeft u enige gezichtsbeharing?\n 1. Ja, ik heb een snor. \n 2. Ja, ik heb een baard. \n 3. Nee, ik heb geen gezichtsbeharing.\n\n")
    if float(vraag8a) == 1:
        (vraag8aa) = input("\nMijn snor is:..cm\n1. 0 t/m 9cm\n2. 10cm of langer\n\n")
        if float(vraag8aa) == 2:
            punten = punten + 1

else:
    vraag8b = input("\nWat voor haar heeft u?\n 1. Ik heb rood gekruld haar. \n 2. Ik heb blond gekruld haar. \n 3. Ik heb bruin gekruld haar.\n\n")
    if float(vraag8b) == 1:
        (vraag8bb) = input("\nMijn haar is:..cm\n1. 0 t/m 10cm\n2. 20cm of langer\n\n")
        if float(vraag8bb) == 2:
            punten = punten + 1

vraag9 = input("\nHoelang bent u?\n 1. 120cm \n 2. 135cm \n 3. 150cm of langer\n\n")
if float(vraag9) == 3:
    punten = punten + 1

vraag10 = input("\nHoe zwaar bent u?\n 1. 80kg \n 2. 85kg \n 3. 90kg of meer\n\n")
if float(vraag10) == 3:
    punten = punten + 1

vraag11 = input("\nBent u in bezit van het 'Overleven met gevaarlijk personeel' certificaat? (y/n)\n\n")
if (vraag11) == "y":
    punten = punten + 1

input("\nDraagt u momenteel een onderbroek? (y/n)\n")
input("\nKan u tot 10 tellen? (y/n)\n")
input("\nHeeft u ooit over de wc-bril geplast? (y/n)\n")
input("\nVindt u deze laatste 4 vragen niet heel raar? (y/n)\n")

if punten < 11:
    print(gefaald)
    exit()

print("\nGefeliciteerd",vraag_naam,", U voldoet aan onze eisen en zult zo spoedig mogelijk van ons horen.")
exit()