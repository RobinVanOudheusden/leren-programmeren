from schoenen_check_data import *

# opdracht 2:
# Vraag een merk en print vervolgens alle modellen van het merk en de bijbehorende prijs.

lijst = []
for i in range(len(schoenen_lijst)):
    if schoenen_lijst [i]['merk'] not in lijst:
        lijst.append(schoenen_lijst[i]['merk'])


gevraagde_schoen = input(f'Welke schoen wil je zien? {lijst} \n')

for schoen in schoenen_lijst:
    if schoen["merk"] == gevraagde_schoen:
        print(schoen['merk'] , schoen['model'] , schoen['prijs'] , schoen['kleur'],)
