from fruitmand import fruitmand
import random

aantal = int(input("Geef een getal: "))

keuze = random.choice(fruitmand)

for z in range(aantal):
    print(keuze['name'])