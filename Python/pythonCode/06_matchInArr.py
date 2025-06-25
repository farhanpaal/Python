# WAP TO FIND/MATCH ELEM OF AN ARRAY
index=0
place=0
def fun(name):
    global index
    global place
    arr=["farhan","sourav","zahid","javid","zahid"]
    data=arr[index]
    if data.lower()==name.lower().strip():
        place=place+1
    index=index+1
    length=len(arr)
    if(index<length): fun(name)
    else: 
        if place>0: print(name,"is matched at",place,"place")
        else: print("not found!")

def app():
    name=input("Enter name: ")
    fun(name)

app()