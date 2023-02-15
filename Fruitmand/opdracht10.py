from fruitmand import fruitmand

lijst = {}

for fruit in range(len(fruitmand)):
    lijst.update({fruitmand[fruit].get('weight')/1000: fruitmand[fruit].get('name')})

print(sorted(lijst.items(), reverse=True))