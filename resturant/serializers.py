from rest_framework import serializers
from .models import Resturant,Images,Address,Menu,ItemType

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

class ResturantSerializer(serializers.ModelSerializer):
    address=AddressSerializer(many=False,read_only=True)
    images=ImageSerializer(many=True,read_only=True)
    menus=MenuSerializer(many=True,read_only=True)
    class Meta:
        model=Resturant
        fields=('id','description','cover_photo','address','images','menus',)





