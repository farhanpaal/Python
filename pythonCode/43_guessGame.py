"""
This is a guessing name built by using while loop
"""
import random as rand


def guess():
  randomNum = rand.randint(0, 10)
  while True:
    try:
      num = int(input("Enter number to guess (0-10): "))
    except:
      print("Wrong input")

    else:
      if num == randomNum:
        print("You win🎉🎉🎇🎆")
        break  # Changed from exit() to break
      else:
        if randomNum > num:
          print("Incorrect: Your entered number too low")
        else:
          print("Incorrect: Your entered number too high ")
        continue

  # This code runs after break (but wouldn't run after exit())
  print("Thanks for playing!")
  print("Game ended.")


guess()
print("Program finished.")  # This also runs with break, but not with exit()
