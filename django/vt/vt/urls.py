from django.urls import path
from django.shortcuts import render

def Home(request):
    return render(request,'index.html',{
        'loveStatus':5000,
        'menus':['home','contact','about us']
    })
def About(request):
    return render(request, 'about.html')
def Contact(request):
    return render(request, 'contact.html')

urlpatterns=[
    path('', Home),
    path('about', About),
    path('contact', Contact)
]