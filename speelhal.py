ticket_pp = 7.45
aantal_personen = int(input('Met hoeveel personen bent u? '))
aantal_min_in_VR = int(input('Hoeveel minuten wilt u in de VR? '))
VR_kost = 0.37

totale_prijs = ticket_pp * aantal_personen + aantal_min_in_VR * (VR_kost / 5 ) * aantal_personen
float = totale_prijs
format_float = "{:.2f}".format(float)


print("Dit geweldige dagje met " + str(aantal_personen) + " mensen in de Speelhal met " + str(aantal_min_in_VR) + " minuten VR kost je maar €" + str(float))
