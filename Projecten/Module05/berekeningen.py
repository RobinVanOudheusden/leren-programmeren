def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

while True:
    keuze = input("Wat wilt u doen? \n(A) Getallen Optellen \n(B) Getallen Aftrekken \n(C) Getallen Vermenigvuldigen \n(D) Getallen Delen \n(E) Getal Ophogen \n(F) Getal Verlagen \n(G) Getal Verdubbelen \n(H) Getal Halveren \n(I) Helemaal Stoppen\n").lower()

    if keuze == "a":
        n1 = float(input("Welk getal optellen: "))
        n2 = float(input(f"Welk getal optellen bij {n1}: "))
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}\n")

    elif keuze == "b":
        n1 = float(input("Welk getal aftrekken: "))
        n2 = float(input(f"Welk getal aftrekken bij {n1}: "))
        uitkomst = subtraction(n1, n2)
        print(f"{n1} - {n2} = {uitkomst}\n")

    elif keuze == "c":
        n1 = float(input("Welk getal vermenigvuldigen: "))
        n2 = float(input(f"Welk getal vermenigvuldigen bij {n1}: "))
        uitkomst = multiplication(n1, n2)
        print(f"{n1} * {n2} = {uitkomst}\n")

    elif keuze == "d":
        n1 = float(input("Welk getal delen: "))
        n2 = float(input(f"Welk getal delen bij {n1}: "))
        uitkomst = division(n1, n2)
        print(f"{n1} / {n2} = {uitkomst}\n")

    elif keuze == "e":
        n1 = float(input("Getal ophogen: "))
        n2 = 1
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}\n")

    elif keuze == "f":
        n1 = float(input("Getal verlagen: "))
        n2 = 1
        uitkomst = subtraction(n1, n2)
        print(f"{n1} - {n2} = {uitkomst}\n")

    elif keuze == "g":
        n1 = float(input("Getal verdubbelen: "))
        n2 = 2
        uitkomst = multiplication(n1, n2)
        print(f"{n1} * {n2} = {uitkomst}\n")

    elif keuze == "h":
        n1 = float(input("Getal halveren: "))
        n2 = 2
        uitkomst = division(n1, n2)
        print(f"{n1} / {n2} = {uitkomst}\n")

    elif keuze =='i':
        print("Oke, dan stoppen we hier!")
        break

    uitkomst1 = uitkomst
    while True:
        keuze_uitkomst = input(f"Wilt u wat met de uitkomst doen? ({uitkomst1}) \n(A) Getallen Optellen \n(B) Getallen Aftrekken \n(C) Getallen Vermenigvuldigen \n(D) Getallen Delen \n(E) Getal Ophogen \n(F) Getal Verlagen \n(G) Getal Verdubbelen \n(H) Getal Halveren \n(I) Helemaal Stoppen\n").lower()

        if keuze_uitkomst == "a":
            n2a = float(input(f"Welk getal optellen bij {uitkomst1}?: "))
            uitkomst1 = uitkomst1 + n2a
            print(f"{uitkomst1}")

        elif keuze_uitkomst == "b":
            n2a = float(input(f"Welk getal aftrekken van {uitkomst1}?: "))
            if n2a > uitkomst1:
                print("Dat getal is te groot om af te trekken. Het getal mag niet negatief worden!")
            else:
                uitkomst1 = uitkomst1 - n2a
                print(f"{uitkomst1}")
    
        elif keuze_uitkomst == "c":
            n2a = float(input(f"Welk getal vermenigvuldigen met {uitkomst1}?: "))
            uitkomst1 = uitkomst1 * n2a
            print(f"{uitkomst1}")

        elif keuze_uitkomst == "d":
            n2a = float(input(f"Welk getal delen met {uitkomst1}?: "))
            if n2a == 0:
                print("Kan getal niet door 0 delen!")
            else:
                uitkomst1 = uitkomst1 / n2a
                print(f"{uitkomst1}")

        elif keuze_uitkomst == "e":
            print("Getal opgehoogd.")
            uitkomst1 = uitkomst1 + 1
            print(f"{uitkomst1}")

        elif keuze_uitkomst == "f":
            print("Getal verlaagd.")
            uitkomst1 = uitkomst1 - 1
            print(f"{uitkomst1}")

        elif keuze_uitkomst == "g":
            print("Getal verdubbeld.")
            uitkomst1 = uitkomst1 * 2
            print(f"{uitkomst1}")

        elif keuze_uitkomst == "h":
            print("Getal gehalveerd.")
            uitkomst1 = uitkomst1 / 2
            print(f"{uitkomst1}")   

        elif keuze_uitkomst == "i":
            print("Oke, dan stoppen we hier!")
            exit()