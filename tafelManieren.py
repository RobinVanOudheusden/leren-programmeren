nummer = input("Vul een nummer in: ")

for i in range (1,11,1):
    x = int(nummer) * i
    print(str(i) + " x " + str(nummer) + " = " + str(x))
    