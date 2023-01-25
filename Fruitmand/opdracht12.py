from fruitmand import fruitmand

kleuren = {
    "yellow" : "gele",
    "green" : "groene",
    "orange" : "oranje",
    "brown" : "bruine",
}

namen = []

for z in range (len(fruitmand)):
    namen.append(fruitmand[z]['name'])
namen.sort(key=len)
namen.reverse()

langste_naam = namen[0]
aantal_letters = len(langste_naam)

for y in range(len(fruitmand)):
    if fruitmand[y]["name"]== langste_naam:
        gewicht = fruitmand[y]["weight"]
        kleur = fruitmand[y]["color"]

print('De', langste_naam, '(' ,aantal_letters, 'letters ) heeft een' ,kleuren[kleur], 'kleur en een gewicht van' ,gewicht/1000,'kg')