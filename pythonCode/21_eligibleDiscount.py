"""
WAP that asks users for their age and gender, and prints message indicating whether they are eligible for a discount . Females under age of 25, males under age of 22 are eligible for a discount.
"""

def main():
  try:
    age= int(input("Enter Your Age: "))
    gender= input("Enter Your Gender: ")
    if gender.lower() != 'female' and gender.lower() != "male":
      print("Invalid gender")
  except:
    print("invalid age")
  else:
    if(gender.lower()=="female" and age<25):
      print("Discount granted")
    elif(gender.lower()=="male" and age<22):
      print("Discount granted")
    else:
      print("No discount for you")
  
main()