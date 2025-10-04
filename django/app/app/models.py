from django.db import models

class Enquiry(models.Model): #inheret modal class and access its all variables,funcs
    name=models.CharField(max_length=100) #we can store 1(00 chars
    email=models.EmailField()
    mobile=models.BigIntegerField()
    message=models.TextField()
    screenshot=models.ImageField(upload_to="images/")
    createdAt=models.DateTimeField(auto_now_add=True)  #it will store date and time of that time