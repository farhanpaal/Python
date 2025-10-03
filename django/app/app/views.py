from django.shortcuts import render
from util.service import SendHtmlMail
# from util.service import SendPlainMail
from .models import Enquiry

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html', {'name': 'Farhan Pala', 'result': 23, 'menus': ['Mobile', 'Laptop', 'Tablet']})

def Contact(request):
    if (request.method) == "POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        data={
            'name':name,
            'email':email,
            'message':message
        }
        res=SendHtmlMail("from TEFAR",
                    'mail/enquiry.html',
                    data,
                    ['farhan.12345.pala@gmail.com'])
        if res['success']:
            enquiry= Enquiry(
                name=name,
                email=email,
                message=message
            )
            enquiry.save()
            return render(request,'success.html')
        else:
            return render(request, 'failed.html', {
                'message':res['message']}
                )

    return render(request, 'contact.html')



# views.py