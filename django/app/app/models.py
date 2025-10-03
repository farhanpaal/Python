from django.db import models

class Enquiry(models.Model): #inheret modal class and access its all variables,funcs
    name=models.CharField(max_length=100) #we can store 1(00 chars
    email=models.EmailField()
    message=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)  #it will store date and time of that time