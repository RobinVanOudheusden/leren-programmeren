import random
kleuren = ("Harten", "Klaveren", "Schoppen", "Ruiten")
combinatie = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas")
mijndeck = []

for x in range (len(combinatie)):
    for y in range (len(kleuren)):
        mijndeck.append(kleuren[y] + ' ' + combinatie[x])

for z in range(2):
    mijndeck.append("Joker")

random.shuffle(mijndeck)

for i in range(7):
    print(f"Kaart" , i+1 , ": " + mijndeck[0])
    mijndeck.pop(0)

print("\nHet gehele deck kaarten: (" + str(len(mijndeck)) + " Kaarten)\n" + str(mijndeck))