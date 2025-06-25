"""
This program calculates BMI
----------------------

Algorithm:
-------------
1. Start
2. Take persons height (in meters)
3. Take persons weight (in kg)
4. If their BMI is less tha 18.5, print underweight
5. If their BMI is between 18.5 and 24.9, print "Normal Weight"
6. If their weight is between 25 and 29.9, print "Overweight".
7. If their BMI is 30 or greater, print "Obese"
8. Stop
"""

def BMI():
  try: 
    height= float(input("Enter persons height in METERS"))
    weight = float(input("Enter persons weight in KILOGRAMS"))
  except ValueError as msg:
    print(msg)
  else:
    bmi= weight/(height*height)
    print(bmi)
    if bmi<18.5 : print("You are Underweight")
    elif bmi < 24.5 : print("You are Normal weight")
    elif bmi < 29.9 : print("You are Overweight")
    else: print("obese")
BMI()
    
  