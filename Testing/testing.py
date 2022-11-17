lijst=[]
for x in range (20):
    vraag = input("welk getal kiest u : ")
    lijst.append(vraag)
lijst.sort()
print ("kleinste getal is ",lijst[0])
print ("grootste getal is ",lijst[19])