from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
for x in range (8):
    robotArm.moveRight()
for y in range (9):
    robotArm.grab()
    color = robotArm.scan()

    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
        
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()