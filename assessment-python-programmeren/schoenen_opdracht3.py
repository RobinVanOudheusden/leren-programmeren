from schoenen_check_data import *


# opdracht 3:
# Vraag een merk en print vervolgens alle witte schoenen mits duurder dan €100.

lijst = []
for i in range(len(schoenen_lijst)):
    if schoenen_lijst [i]['merk'] not in lijst:
        lijst.append(schoenen_lijst[i]['merk'])


gevraagde_merk = input(f'Welke schoen wil je zien? {lijst} \n')

for schoen in schoenen_lijst:
    if schoen["merk"] == gevraagde_merk and schoen["kleur"] == "wit" and schoen["prijs"] > 100:
        print(schoen['merk'] , schoen['model'] , schoen['prijs'] , schoen['kleur'],)
    