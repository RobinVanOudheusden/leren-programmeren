kerenGevraagd = 1

repeat = True
while repeat == True:
    vraag = input("Wil je stoppen? (y/n):\n")

    if vraag == "y":
        print("Oke doei! De vraag is" , kerenGevraagd , "keer gesteld tot je stopte.")
        repeat = False

    elif vraag == "n":
        print("Nog maar een keertje dan!")
        kerenGevraagd = kerenGevraagd + 1
        repeat = True

    







