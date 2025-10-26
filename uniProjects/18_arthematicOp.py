# basic arthematic operation
print("| This is a program for basic arthemetic operation | ")
while True:
    try:
        firstNo= int(input("\nEnter first Number: "))
        secondNo= int(input("Enter second Number: "))

        
        store=int(input("What do you want to do: \n 1) Addition \n 2) Subtraction \n 3) Multiplication \n 4) Division \n"))

        if(store==1):
            print(f"The sum of {firstNo} and {secondNo} is: {firstNo+secondNo}")
        elif(store==2):
            print(f"The Subtraction of {firstNo} and {secondNo} is: {firstNo-secondNo}")

        elif(store==3):
            print(f"The multiplication of {firstNo} and {secondNo} is: {firstNo*secondNo}")
        elif(store==4):
            if(secondNo==0):
                print("Undefined! Second number is a denominator, and denominator can never be zero")
            else:
                print(f"The division of {firstNo} and {secondNo} is: {firstNo/secondNo}")
    except ValueError as ve: 
        print("Wrong input! ", ve)
        continue
    
    else:
        print("-"*40)
        print("Do you want to continue or stop here (1:continue, 0:stop")
        store= int(input("Enter your choice: "))
        if(store==1):
            continue
        elif(store==0):
            break
        
        


