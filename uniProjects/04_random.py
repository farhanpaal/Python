"""
Program 1
------------------------------
1:Start
2:Import random library
3:Store random number in a variable
4:Print variable
5:End

"""

import random as rand
import time 


def randomNum():
  a=rand.randint(1,10)
  print(a)
# randomNum()
print("-"*50)

"""
Program 2
---------------------------------
1:Start
2:Use loop to print 10 random numbers after every one second
3:
"""

def loopRand():
  for i in range(10):
    print(rand.randint(1,9))
    time.sleep(1)
# loopRand()
print("-"*50)

"""
Program 2
---------------------------------
1:Start
2:Define 2 lists: player1, player2
3:create 2 variables, x, y which will store random numbers
4:if input == nu
    
"""
def diceGame():
  player1=[]
  player2=[]
  y=6
  for i in range(y):
    
    input("Press 'ENTER' to generate random numbers") 
   
    
    dice1= rand.randint(1,6)
    dice2= rand.randint(1,6)
    player1.append(dice1)
    player2.append(dice2)
    print(player1)
    print(player2)

  sum1= sum(player1)
  sum2= sum(player2)
  if sum1>sum2:
    print("Player1 won the game")
  elif sum1==sum2:
    print("DRAW")
  else:
    print("Player2 Won the game")
  print(f"Player1 score: {sum1} \nPlayer2 score: {sum2} ")
  
diceGame()