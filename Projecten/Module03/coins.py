# name of student: Robin van Oudheusden
# number of student: 99071681@mydavinci.nl
# purpose of program: 
# function of program:
# structure of program: 

euro5 = 0
euro3 = 0
euro2 = 0
euro1 = 0
cent50 = 0
cent20 = 0
cent10 = 0
cent5 = 0
cent2 = 0
cent1 = 0

toPay = int(float(input('Amount to pay: '))* 100) 
paid = int(float(input('Paid amount: ')) * 100) 
change = paid - toPay 

if change > 0: 
  coinValue = 500 
  
  while change > 0 and coinValue > 0: 
    nrCoins = change // coinValue 

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue 

# comment on code below: Wisselgeld
    if coinValue == 500:
      euro5 = nrCoinsReturned
      coinValue = 300
    elif coinValue == 300:
      euro3 = nrCoinsReturned
      coinValue = 200
    elif coinValue == 200:
      euro2 = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      euro1 = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      cent50 = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      cent20 = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      cent10 = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      cent5 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      cent2 = nrCoinsReturned
      coinValue = 1
    elif coinValue == 1:
      cent1 = nrCoinsReturned
      coinValue = 0
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
  print("|BON                                 |")
  print("|5  euro:                  " + str(euro5) +"x")
  print("|3  euro:                  " + str(euro3) +"x")
  print("|2  euro:                  " + str(euro2) +"x")
  print("|1  euro:                  " + str(euro1) +"x")
  print("|50 cent:                  " + str(cent50) +"x")
  print("|20 cent:                  " + str(cent20) +"x")
  print("|10 cent:                  " + str(cent10) +"x")
  print("|5  cent:                  " + str(cent5) +"x")
  print("|2  cent:                  " + str(cent2) +"x")
  print("|1  cent:                  " + str(cent1) +"x")
  print("_____________________________________")