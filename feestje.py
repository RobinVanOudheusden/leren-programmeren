gastheer = input("Wat is de naam van de gastheer?: \n")
gasten = 5
gasten = int(gasten)
drank = True
chips = True
niet_welkom = "Rudi"

if not gastheer == niet_welkom and drank == True and gasten == 0 or not gastheer == niet_welkom and drank == True and gasten < 12 and drank and chips or not gastheer == niet_welkom and drank == True and gasten <=12 and gasten > 5:
    print("Het feestje kan beginnen!")

else:
    print ("No party today! ):")

