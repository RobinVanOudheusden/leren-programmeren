from schoenen_check_data import *

# opdracht 4:
# vraag de maat van de klant en print vervolgens:
# "fonetische_kleuren Merknaam Modelnaam, prijs"
# uiteraard alleen de schoenen die beschikbaar zijn in betreffende maat.

schoen_maat = int(input('Welke maat schoen wil je zien? \n'))

for schoen in schoenen_lijst:
    if schoen_maat in schoen['maten']:
        print(schoen['kleur'] , schoen['merk'] , schoen['model'] , schoen['prijs'] , schoen['kleur'],)

