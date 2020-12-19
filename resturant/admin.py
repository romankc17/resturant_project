from django.contrib import admin
from .models import Resturant,Address,Menu,ItemType,Images


class MenuInline(admin.StackedInline):
    model=Menu
    extra = 0

# class AddressInline(admin.StackedInline):
#     model = Address

class ResturantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name']}),
        ('Bio',{'fields':['description']}),
        ('Address',{'fields':['address']}),
    ]
    inlines = [MenuInline]

admin.site.register([Resturant,Address,Menu,ItemType,Images])
# admin.site.register(Resturant,ResturantAdmin)