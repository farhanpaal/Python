from django.urls import path
from .views import Home, About, Contact

urlpatterns=[
    path('', Home),
    path('about', About),
    path('contact', Contact),
]