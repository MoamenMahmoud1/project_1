from django.contrib import admin
from .models import *



# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'price' , 'active' , 'category']
    list_display_links = ['name']
    list_editable = ['price' , 'active' , 'category']
    search_fields = ['name']
    list_filter = ['category' , 'active']
    fields = ['name']
    

# Register Product model on the admin interface
# This will allow the admin to add, edit, and delete products from the interface

admin.site.register(Test)
admin.site.register(Product, productAdmin)
admin.site.site_header = " E    4    Y"
admin.site.site_title = " E    4    Y"
