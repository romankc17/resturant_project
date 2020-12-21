from django.db import models
from django.db.models import Avg
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Address(models.Model):
    district=models.CharField(max_length=50)
    province=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    tole=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.city}->{self.tole}'

    class Meta:
        verbose_name_plural = "Addresses"

class PhoneNumber(models.Model):
    number=models.CharField(max_length=10,blank=True)

class Contact(models.Model):
    facebook=models.URLField(max_length=100,blank=True)
    instagram=models.URLField(max_length=100,blank=True)
    email = models.EmailField(blank=True,max_length=100)
    phone_number=models.ForeignKey(PhoneNumber,on_delete=models.CASCADE)
    website=models.URLField(max_length=100,blank=True)

def get_cover_image_filename(instance, filename):
    title = instance.name
    slug = slugify(title)
    return "%s/cover_image/%s" % (slug, filename)

class Resturant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500,blank=True)
    cover_photo=models.ImageField(upload_to=get_cover_image_filename)
    address = models.OneToOneField(Address, on_delete=models.CASCADE,related_name='address')
    delivery_available = models.BooleanField(default=False)
    open_time = models.TimeField(blank=True,null=True)
    close_time = models.TimeField(blank=True,null=True)
    contact = models.OneToOneField(Contact,null=True,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.name

    def stars_average(self):
        self.review_set.aggregate(Avg('stars')).values()[0]
    stars_average.short_description='Ratings'

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    resturant = models.ForeignKey(Resturant,on_delete=models.CASCADE,)
    review = models.TextField(max_length=500,blank=True,null=True)
    stars = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],null=True,blank=True)
    reviewed_on = models.DateField(auto_now_add=True,null=True,blank=True)

def get_menu_image_filename(instance, filename):
    title = instance.resturant.name
    slug = slugify(title)
    return "menu_images/%s-%s" % (slug, filename)

class ItemType(models.Model):
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Menu(models.Model):
    resturant = models.ForeignKey(Resturant,on_delete=models.CASCADE,related_name='menus')
    item=models.CharField(max_length=50)
    item_photo = models.ImageField(upload_to=get_menu_image_filename,null=True,blank=True)
    item_type=models.ForeignKey(ItemType,on_delete=models.CASCADE)
    price=models.IntegerField()

def get_resturant_image_filename(instance, filename):
    title = instance.resturant.name
    slug = slugify(title)
    return "resturant_images/%s-%s" % (slug, filename)

class Images(models.Model):
    resturant=models.ForeignKey(Resturant,default=None,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to=get_resturant_image_filename,verbose_name='Image',null=True,blank=True)

    def __unicode__(self):
        return self.id