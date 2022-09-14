import math

#Robin van Oudheusden
#99071681
#Opdracht pizzaCalculator

small = 6.99
medium = 9.99
large = 12.99

keuze = input('wilt u small, medium of large pizza?: ')
aantal = input('hoeveel pizzas zou u willen?: ')

prijs = 0

if keuze == "small":
    prijs = int(aantal) * small

if keuze == "medium":
    prijs = int (aantal) * medium

if keuze == "large":
    prijs = int (aantal) * large

print("\nde prijs is €",prijs,"")

print("-------------------------------")
print("|",aantal , 'x', keuze," pizza")
print("| het totale bedrag is: €",prijs,)
print("-------------------------------")