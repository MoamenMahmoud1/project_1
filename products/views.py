from django.shortcuts import render
from .models import Product 

# Create your views here.
def product(request):
    return render(request, 'products/product.html')
def products(request):
    #aha = Product.objects.filter(category='phone')
    #aha = Product.objects.all().order_by('name')
    #aha = Product.objects.get(id=4)
    #aha = str(Product.objects.count())
    #aha = Product.objects.exclude(id=4)                                                            
    #aha = Product.objects.filter(price__exact=100)                                                 
    #aha = Product.objects.filter(price__lte=100)                               #__lte -> Less than or equal
    #aha = Product.objects.filter(price__gte=100)                               #__gte -> Greater than or equal
    #aha = Product.objects.filter(price__lt=100)                                #__lt -> Less than
    #aha = Product.objects.filter(price__gt=100)                                #__gt -> Greater than
    #aha = Product.objects.filter(price__range=(100,200))
    #aha = Product.objects.filter(name__contains='h')
    #aha = Product.objects.filter(name__startswith='h')
    #aha = Product.objects.filter(name__endswith='a')
    aha = Product.objects.filter(price__in=[100,200 , 300])
    
    x = {'pro':aha}
    return render(request, 'products/products.html' , x)
