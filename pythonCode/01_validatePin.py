# wap to make login system where codition is pin limit and only accepts numbers 

def ValidatePin(pin):
    if len(pin)<=5 and pin.isdigit():
        return True
    else:
        return False
    
def chkPin():
    pin= input("Enter pin: ")
    if ValidatePin(pin):
        print("right")
    else:
        print("False")

chkPin();
