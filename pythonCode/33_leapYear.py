def leap():
  try:
    year= int(input("Enter the year"))
  except:
    raise Exception ("Wrong input")
  else:
    if year/4==0:
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not a leap year")
leap()

