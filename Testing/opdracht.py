from data import *

# opdracht 2:
# Vraag een merk en print vervolgens alle modellen van het merk en de bijbehorende prijs.
lijst = []
for i in range(len(schoenen_lijst)):
    if schoenen_lijst [i]['merk'] not in lijst:
        lijst.append(schoenen_lijst[i]['merk'])




gevraagd_merk = input(f'Welke schoen wil je zien? {lijst} ')

for schoen in schoenen_lijst:
    if schoen["merk"] == gevraagd_merk:
        print(schoen['merk'] , ['model'] , ['prijs'] , ['kleur'],)