# WAP print data from list using recursion

lst=["hello","topg","here"]
length= len(lst)
idx=0
def fun():
    global idx;
    print(lst[idx])
    idx=idx+1
    if(idx<length): fun()

fun()