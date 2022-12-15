from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

x = 9
for y in range(5):
    robotArm.grab()
    for z in range(x):
        robotArm.moveRight()
    x -= 1
    robotArm.drop()
    for z in range(x):
        robotArm.moveLeft()
    x -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()