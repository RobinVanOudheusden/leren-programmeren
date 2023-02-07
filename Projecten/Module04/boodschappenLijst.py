repeat = True
boodschappenlijst = {}

while repeat == True:
    toevoegen = input("Wat wilt u toevoegen aan uw boodschappenlijstje?\n").upper()
    aantal = int(input(f"Hoe vaak wilt u {toevoegen} aan uw lijstje toevoegen?\n"))

    if toevoegen not in boodschappenlijst:
        boodschappenlijst.update({toevoegen:aantal})

    else:
        (boodschappenlijst)[toevoegen] += (aantal)

    restart = input("Wilt u nog wat toevoegen?: (y/n)\n")

    if restart == ("n"):
        break

print("=[-| BOODSCHAPPENLIJSTJE |-]=")
for aantal, toevoegen in boodschappenlijst.items():
    print(f"{toevoegen} x {aantal}")
print("=[-]-[-]-[-]-[-]-[-]-[-]-[-]=")