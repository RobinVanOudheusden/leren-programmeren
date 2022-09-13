
repeat = True

while repeat == True:
    print("is de kaas geel?: (y/n)")
    vraag = input().lower()
        
    if vraag == "y":
        print("zitten er gaten in?: (y/n)")
        repeat = True
        vraag = input().lower()
        
        if vraag == "y":
            print("is de kaas belachelijk duur?: (y/n)")
            repeat = True
            vraag = input().lower()
            if vraag == "y":
                repeat = False
                print("het is emmenthaler.")
            elif vraag == "n":
                print("het is leerdammer kaas.")
                repeat = False

        elif vraag == "n":
            print("is de kaas hard als een steen?: (y/n)")
            repeat = True
            vraag = input().lower()

            if vraag == "y":
                print("het is parmigiano reggiano.")
                repeat = False
                vraag = input().lower()
            elif vraag == ("n"):
                print("het is goudse kaas.")
                repeat = False
                vraag = input().lower()
    
    elif vraag == ("n"):
        print("heeft de kaas blauwe schimmel?: (y/n)")
        repeat = True
        vraag = input().lower()

        if vraag == ("ja"):
            print("heeft de kaas een korst?: (y/n)")
            repeat = True
            vraag = input().lower()
            
            if vraag == ("y"):
                print("het is blue de rockbaron.")
                repeat = False
                vraag = input().lower()
            elif vraag == ("n"):
                print ("het is foume d'ambert.")
                repeat = False
                vraag = input().lower()
        elif vraag == ("n"):
            print("heeft de kaas een korst? (y/n)")
            repeat = True
            vraag = input().lower()

            if vraag == ("y"): 
                print("het is camembert.")
                repeat = False
                vraag = input().lower()
            elif vraag == ("n"):
                print("het is mozzarella.")
                repeat = False
                vraag = input().lower()
            