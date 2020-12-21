from django.contrib import admin
from .models import *

class ReviewsInline(admin.StackedInline):
    model = Review
    extra=0

class MenuInline(admin.StackedInline):
    model=Menu
    extra = 0


# class AddressInline(admin.StackedInline):
#     model = Address

class ResturantAdmin(admin.ModelAdmin):
    list_display=('name','address','stars_average')
    inlines = [MenuInline,ReviewsInline]

# admin.site.register([Resturant,Address,Menu,ItemType,Images])
admin.site.register(Resturant,ResturantAdmin)