from django.db import models
from django.contrib.auth.models import User

#واحد لواحد
class Female(models.Model):
    name_female = models.CharField(max_length=5 , null = True)
    def __str__(self):
        return self.name_female

class Male(models.Model):
    name_male = models.CharField(max_length=5 , null=True)
    girls = models.OneToOneField(Female , on_delete=models.PROTECT) #or on_delete=models.CASCADE
    def __str__(self):
        return self.name_male


#واحد لعديد 
class Product(models.Model):
    title = models.CharField(max_length=50 , null=True)
    
    def __str__(self):
        return self.title
class User(models.Model):
    name = models.CharField(max_length=50 , null=True)
    products = models.ForeignKey(Product , on_delete=models.CASCADE)
   
   
#كثير لكثير 


    
    
class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username
    

