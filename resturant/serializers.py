from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields=('id','image')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields='__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields='__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        models=Feature
        fields='__all__'

class ResturantSerializer(serializers.ModelSerializer):
    address=AddressSerializer(many=False,read_only=True)
    reviews=ReviewSerializer(many=True,read_only=True)
    contact=ContactSerializer(many=False,read_only=True)
    images=ImageSerializer(many=True,read_only=True)
    menus=MenuSerializer(many=True,read_only=True)
    features=FeatureSerializer(many=True,read_only=True)
    class Meta:
        model=Resturant
        fields=('id','description','open_time','close_time','delivery_available','cover_photo','address','images','features','menus','contact','reviews')





