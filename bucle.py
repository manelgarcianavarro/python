import random
robot = random.randint(1,3)
if ( robot == 1) :

    robot = "papel"


if (robot == 2) :

    robot = "tijera"


if (robot == 3) :

    robot = "piedra"

print("Elige")
user = input()
print(robot)

if robot == "papel" :

    if user == "piedra":
    
        print("Robot Win")
    

    if user == "papel" :
    
        print("Tie")
    

    if user == "tijera" :
    
        print("User Win")
    


if robot == "piedra" :

    if user == "tijera" :
    
        print("Robot Win")
    

    if user == "piedra" :
    
        print("Tie")
    

    if user == "papel" :
    
        print("User Win")
    


if robot == "tijera" :

    if user == "papel" :
    
        print("Robot Win")
    

    if user == "tijera" :
    
        print("Tie")
    

    if user == "piedra" :
    
        print("User Win")
    
