from fruitmand import fruitmand

repeat = True
lijstkleuren = []

rond = 0
niet_rond = 0

for x in range(len(fruitmand)):
    kleur = (fruitmand[x]['color'])
    if kleur not in lijstkleuren:
        lijstkleuren.append(kleur)
while repeat == True:
    kleur = str(input("Kies een kleur uit de kleuren : " + str(lijstkleuren)+"?\n")).lower()
    if (kleur) not in lijstkleuren:
        print ("De Kleur " + kleur + " zit niet in de fruitmand")
    else:
        print("Kleur zit in de lijst.")
        repeat = False
for fruit in fruitmand:
            if fruit['color'] == kleur:
                if fruit['round'] == True:
                    rond += 1
                else:
                    niet_rond += 1

verschil = abs(rond - niet_rond)

if rond > niet_rond:
    print (f"Er zijn {int(verschil)} meer ronde vruchten dan niet ronde vruchten in de kleur {str(kleur)}")
if rond < niet_rond:
        print (f"Er zijn {str(verschil)} minder ronde vruchten dan niet ronde vruchten in de kleur {str(kleur)}")
if rond == niet_rond:
    print (f"Er zijn {str(verschil)} ronde vruchten en {str(niet_rond)} niet ronde vruchten in de kleur {str(kleur)}")
