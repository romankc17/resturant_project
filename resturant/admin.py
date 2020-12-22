from django.contrib import admin
from .models import *

class ReviewsInline(admin.StackedInline):
    model = Review
    extra=0

class MenuInline(admin.StackedInline):
    model=Menu
    extra = 0

class ImagesInline(admin.StackedInline):
    model = Images
    extra = 0

class ResturantAdmin(admin.ModelAdmin):
    list_display=('name','address','show_average_ratings')
    inlines = [MenuInline,ImagesInline,ReviewsInline]

admin.site.register([Address,ItemType,Review,Contact])
admin.site.register(Resturant,ResturantAdmin)