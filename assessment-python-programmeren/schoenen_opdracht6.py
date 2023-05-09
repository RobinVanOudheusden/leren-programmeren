from schoenen_check_data import *

# opdracht 6:
# print van de schoen leverbaar in de grootste maat :
# IN maat ... leverbaar: merk. model en kleur van de schoenen

grootste_maat = 0

for schoen in schoenen_lijst:
    for maat in schoen["maten"]:
        if maat > grootste_maat:
            grootste_maat = maat
            grootste_maatschoenen = [(schoen["merk"], schoen["model"], schoen["kleur"])]
        elif maat == grootste_maat:
            grootste_maatschoenen.append((schoen["merk"], schoen["model"], schoen["kleur"]))


print(f"IN maat {grootste_maat} leverbaar: ")
for schoen in grootste_maatschoenen:
    kleur = fonetische_kleuren[schoen[2]] if schoen[2] in fonetische_kleuren else schoen[2]
    print(f"{schoen[0]}. {schoen[1]} in {kleur}")
