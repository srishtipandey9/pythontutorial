### snake water and gun game
## same for stone parer scissor game
print("welcome to snake, water and gun game")
import random
game=["snake","water","gun"]
choice=random.choice(game)
n=0
user =0
computer=0
limit=10

print("you have n number of turns")
while(n<=limit):
    n=n+1
    value=str(input("enter your turn"))
    print(choice)
    if value=="snake" and choice=="water":
      print("user wins")
      user+=1
    elif value=="snake"and choice=="gun":
      print("computer wins")
      computer+=1
    elif value=="gun"and choice== "water":
      print("computer wins")
      computer+=1
    elif value=="water" and choice=="gun":
      print("user wins")
      user+=1
    elif value=="water" and choice=="snake":
      print("computer wins")
      computer+=1
    elif value=="gun"and choice== "water":
      print("user wins")
      user+=1
    elif value=="gun" and choice=="snake":
      user+=1
    elif value=="snake" and choice=="water":
        user+=1
    elif value=="snake" and choice=="snake" or value=="gun=" and choice=="gun"or value=="water" and choice=="water":
        print("draw is there")
    else:
        print("you have entered wrong ")


print("total user wins",user)
print("total computer ",computer)
if user>computer:
    print("over all user won the snake water game")
elif user<computer:
    print("computer won the snake water game")
else:
    print("you have draw")







