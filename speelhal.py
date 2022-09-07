ticket_pp = 7.45
aantal_personen = 4
aantal_min_in_VR = 45
VR_kost = 0.37

totale_prijs = ticket_pp * aantal_personen + (aantal_min_in_VR / 9)  * VR_kost * aantal_personen

print("Dit geweldige dagje met " + str(aantal_personen) + " mensen in de Speelhal met " + str(aantal_min_in_VR) + " minuten VR kost je maar €" + str(totale_prijs))
