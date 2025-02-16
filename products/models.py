from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    
    x = [
        ('phone','phone'),
        ('computer','computer'),
        
    ]
    
    name = models.CharField(max_length=100 , default='hala')
    content = models.TextField(null=True , blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/' , default='photos/2024/12/09/Screenshot_2024-11-08_132430.png' , verbose_name='photos')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50 , null=True , blank=True , choices=x)
    def __int__(self):
        return self.name
    class Meta:
        verbose_name = 'Name'
    
class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created  = models.DateTimeField(default=datetime.now)
    
    
    

    
    