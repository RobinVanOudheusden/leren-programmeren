from fruitmand import fruitmand

kleurenlist = []
for fruit in fruitmand:
    if fruit['name']=='druif':
        fruitmand.remove(fruit)

for i in range(len(fruitmand)):
    if fruitmand[i]['color'] not in kleurenlist:
        kleurenlist.append(fruitmand[i]['color'])
        
print(kleurenlist)