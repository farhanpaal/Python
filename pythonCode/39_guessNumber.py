import random as rand
def guess():
  randNum= rand.randint(1,10)
  while True:
    try:
      num= int(input("Enter Number to gues between 1 to 10: "))
    except:
      print("Invalid number")
    else:
      if(num==randNum):
        print(":) Theek chuy ✨✨🎉🎉")
        exit()
      elif num<randNum:
        print("Entered number is low")
      elif num>randNum:
        print("Entered number is High")
      else:
        print("chah doud daama")
guess()