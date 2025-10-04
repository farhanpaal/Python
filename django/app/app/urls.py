from django.urls import path
from .views import Home, About, Contact
from django.contrib import admin  #for django adminstration
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('', Home),
    path('about', About),
    path('contact', Contact),
    path('admin', admin.site.urls) #activate admin panel for database
]+static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
    )