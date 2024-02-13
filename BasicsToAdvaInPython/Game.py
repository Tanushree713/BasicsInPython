# Snake , Water , Gun Game #
import random 

def gameWin(comp , you ):
    if comp == you :
        return None
    if comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    if comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    if comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True        

randomNo = random.randint(1, 3)
print("Comps's Turn :")
you = input("Your's Turn : Snake(s) , Water(w) , Gun(g) ? ")
if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'w'
elif randomNo == 3:
    comp = 'g'   

print(f"Computer Chose: {comp}")     
print(f"You Chose :{you}" )
result = gameWin(comp , you)    
if result is None :
    print("Game Is Tie !!")
elif result :
    print("You Win!!")
else:
    print("You Lose!!")        

               

