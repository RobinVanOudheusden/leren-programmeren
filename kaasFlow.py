
repeat = True

while repeat == True:
    print("Is de kaas geel?: (y/n)")
    vraag = input().lower()
        
    if vraag == "y":
        print("Zitten er gaten in?: (y/n)")
        repeat = True
        vraag = input().lower()
        
        if vraag == "y":
            print("Is de kaas belachelijk duur?: (y/n)")
            repeat = True
            vraag = input().lower()
            if vraag == "y":
                repeat = False
                print("Het is Emmenthaler.")
            elif vraag == "n":
                print("Het is Leerdammer kaas.")
                repeat = False

        elif vraag == "n":
            print("Is de kaas hard als een steen?: (y/n)")
            repeat = True
            vraag = input().lower()

            if vraag == "y":
                print("Het is Parmigiano Reggiano.")
                repeat = False
                vraag = input().lower()
            elif vraag == ("n"):
                print("Het is Goudse kaas.")
                repeat = False
                vraag = input().lower()
    
    elif vraag == ("n"):
        print("Heeft de kaas blauwe schimmel?: (y/n)")
        repeat = True
        vraag = input().lower()

        if vraag == ("ja"):
            print("Heeft de kaas een korst?: (y/n)")
            repeat = True
            vraag = input().lower()
            
            if vraag == ("y"):
                print("Het is Blue de Rockbaron.")
                repeat = False
                vraag = input().lower()
            elif vraag == ("n"):
                print ("Het is Foume d'Ambert.")
                repeat = False
                vraag = input().lower()
        elif vraag == ("n"):
            print("Heeft de kaas een korst? (y/n)")
            repeat = True
            vraag = input().lower()

            if vraag == ("y"): 
                print("Het is Camembert.")
                repeat = False
                vraag = input().lower()
            elif vraag == ("n"):
                print("Het is Mozzarella.")
                repeat = False
                vraag = input().lower()
            