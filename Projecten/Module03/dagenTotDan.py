dagvandeweek = input("Welke dag is het? ma/di/wo/do/vr/za/zo : \n")
ma = "maandag"
di = "dinsdag"
wo = "woensdag"
do = "donderdag"
vr = "vrijdag"
za = "zaterdag"
zo = "zondag"

while dagvandeweek == "ma":
    print(di, wo, do, vr, za, zo)
    break

while dagvandeweek == "di":
    print(di, wo, do, vr, za, zo, ma)
    break

while dagvandeweek == "wo":
    print(wo, do, vr, za, zo, ma, di)
    break

while dagvandeweek == "do":
    print(do, vr, za, zo, ma, di, wo)
    break

while dagvandeweek == "vr":
    print(vr, za, zo, ma, di, wo, do)
    break

while dagvandeweek == "za":
    print(za, zo, ma, di, wo, do, vr)
    break

while dagvandeweek == "zo":
    print(zo, ma, di, wo, do, vr, za)
    break