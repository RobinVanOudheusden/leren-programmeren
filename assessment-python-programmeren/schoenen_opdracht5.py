from schoenen_check_data import *

# Opdracht 5:
# print van de duurste schoen: merk en model en doe dat ook voor de goedkoopste.

duurste_schoen = 0
goedkoopste_schoen = 1000000000000

for schoen in schoenen_lijst:
    if schoen['prijs'] > duurste_schoen:
        duurste_schoen = schoen['prijs']
        duurste_merk = schoen['merk']
        duurste_model = schoen['model']
    if schoen['prijs'] < goedkoopste_schoen:
        goedkoopste_schoen = schoen['prijs']
        goedkoopste_merk = schoen['merk']
        goedkoopste_model = schoen['model']

print(f'De duurste schoen is {duurste_merk} {duurste_model} en kost {duurste_schoen}')
print(f'De goedkoopste schoen is {goedkoopste_merk} {goedkoopste_model} en kost {goedkoopste_schoen}')

