import random
#snake water gun or rock paper scissors
def game(comp,you): #game RULES----->
    # if tow value are equal,declare a tie!
    if comp==you:
        return None
    # check for  all possibilities when computer chose S
    elif comp== 's':
        if you== 'w':
            return False
        elif you=='g':
            return True
    # check for all possibilities when computer chose W
    elif comp== 'w':
        if you== 'g':
            return False
        elif you=='s':
            return True
    # chek for all possibilities when computer chose G
    elif comp== 'g':
        if you== 's':
            return False
        elif you=='w':
            return True  #---->

print("Comp Turn: Sanke(s), Water(w), or Gun(g)? ->")
randNO = random.randint(1,3)
# print(randNO)
if randNO==1:
    comp = 's'
elif randNO==2:
    comp= 'w'
elif randNO==3:
    comp = 'g'

you = input("Your Turn: Sanke(s), Water(w), or Gun(g)? ->")

a = game(comp,you)

print(f"Computer chose {comp} ")
print(f"You chose {you} ")

if a == None:
    print("The game is a tie!!!")
elif a:
    print("You win!!!")
else:
    print("You LOOS!!")