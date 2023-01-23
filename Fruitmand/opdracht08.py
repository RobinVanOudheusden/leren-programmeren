from fruitmand import fruitmand

totaal_gewicht = 0

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2800,
    'color' : 'red',
    'round' : True})

for fruit in range(len(fruitmand)):
    gewicht = fruitmand[fruit]['weight']
    totaal_gewicht = totaal_gewicht + gewicht

print(f"Totaal gewicht fruit: ",{totaal_gewicht})
