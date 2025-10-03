from django.urls import path
from .views import Home, About, Contact
from django.contrib import admin  #for django adminstration

urlpatterns=[
    path('', Home),
    path('about', About),
    path('contact', Contact),
    path('admin', admin.site.urls) #activate admin panel for database
]