def vragen():
    naam = input("Voer naam in:\n")
    leeftijd = input("Voer leeftijd in:\n")
    return {'naam': naam, 'leeftijd': leeftijd}

lijst = []
repeat = True

while repeat == True:
    persoon = vragen()
    lijst.append(persoon)
    door = input("Wilt u nog een persoon toevoegen?: (y/n)\n").lower()
    if door == 'n':
        break

for persoon in lijst:
    print(persoon['naam'], "is", persoon['leeftijd'], "jaar.")