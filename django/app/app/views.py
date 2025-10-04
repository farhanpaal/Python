from django.shortcuts import render, redirect #redirect fot redirecting to other page, instead of render
from util.service import SendHtmlMail
# from util.service import SendPlainMail
from .models import Enquiry
from django.conf import settings

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html', {'name': 'Farhan Pala', 'result': 23, 'menus': ['Mobile', 'Laptop', 'Tablet']})

def Contact(request):
    if (request.method) == "POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        screenshot=request.FILES['screenshot']
        message=request.POST.get('message')
        print(mobile,screenshot)
        data={
            'name':name,
            'email':email,
            'mobile':mobile,
            'screenshot':screenshot,
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
                mobile=mobile,
                screenshot=screenshot,
                message=message
            )
            enquiry.save()
            return redirect('/contact')
        else:
            return render(request, 'failed.html', {
                'message':res['message']}
                )
    
    data=Enquiry.objects.all().values()
    return render(request, 'contact.html',{'data':data, 'settings':settings})



# views.py