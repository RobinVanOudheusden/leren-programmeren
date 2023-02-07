import random
mm = ('Oranje' , 'Blauw', 'Groen', 'Bruin')
extra = []
aantal = input('Hoeveel m&ms wilt u toevoegen?:\n')

for x in range(int(aantal)):
    bijvoegen = random.choice(mm)
    extra.append(bijvoegen)
    
print(extra)