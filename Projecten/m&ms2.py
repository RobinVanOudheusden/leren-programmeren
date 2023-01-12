import random

kleuren = ('Rood' , 'Blauw', 'Groen', 'Geel', 'Bruin')
aantal = int(input('Hoeveel m&ms wilt u toevoegen?:\n'))
zak = {}
getal = 1

for x in range(aantal):
    kleur = random.choice(kleuren)
    if kleur not in zak:
        zak.update({kleur:getal})
    elif kleur in zak:
        zak[kleur] += 1

print(zak)