from django.shortcuts import render
from util.service import SendMail
def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html', {'name': 'Farhan Pala', 'result': 23, 'menus': ['Mobile', 'Laptop', 'Tablet']})

def Contact(request):
    if (request.method) == "POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        res=SendMail("enquiry from " + name, message, ['ethical.pala.cyber@gmail.com'])
        print(res)
    return render(request, 'contact.html')

