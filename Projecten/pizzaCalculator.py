import math

#Robin van Oudheusden
#99071681
#Opdracht pizzaCalculator

repeat = True

while repeat == True:
    pizza_size = input("Wilt u small, medium of large pizza? ")

    if pizza_size == 'small':
        repeat = False
        prijs= 6.99
    elif pizza_size == 'medium':
        repeat = False
        prijs= 9.99
    elif pizza_size == 'large':
        repeat = False 
        prijs= 12.99
else:
    print(pizza_size)

pizza_aantal = input('hoeveel pizzas wilt u? ' '')

try:
    totaal= int(pizza_aantal) * prijs
except: 
    print("dat is geen cijfer")
    exit()

print("-------------------------------")
print("|",str(pizza_aantal) , 'x', str(pizza_size)," pizza")
print("| het totale bedrag is: €",totaal,)
print("-------------------------------")