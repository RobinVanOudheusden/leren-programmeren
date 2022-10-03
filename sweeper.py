from random import randint

play = True
ronde = 1
bomb = randint(1,30)
score = 0

while play == True:
    guess = input("Ronde "+str(ronde)+": Op welk getal denkt u dat de bom niet ligt\n")
    
    ronde = ronde + 1

    vraag = input("Wilt u naar ronde "+str(ronde)+" (Y/N?)\n").lower()
    
    if vraag == "n":
        play = False
    
        

        