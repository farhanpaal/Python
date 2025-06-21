# idx=0
# a=int(input("enter the number you want to find table of: "))
# def name():
#     global idx
#     idx= idx+1
#     print(a,"*",idx,"=",a*idx)
#     if(idx<10):  name()
#     else: print("recurssion ended")

   

# name()
index=0
def table(a):
    global index
    index=index+1
    print(a,"*",index,"=",a*index)
    if index <20 : table(a)
    else: print("Thank You")

def app():
    num= int(input("Enter a number"))
    table(num)

app()