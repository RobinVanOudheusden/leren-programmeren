from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

z = 0
y = 1

for a in range(8):
    robotArm.moveRight()

for b in range(9):
    robotArm.grab()
    color = robotArm.scan()
    z = z + 1
    y = y + 1

    if color == "red":
        for c in range(z):
            robotArm.moveRight()
        robotArm.drop()
        for d in range(y):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()