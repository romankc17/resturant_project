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
        extra_kwargs={
            'id':{'read_only':True}
        }

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=('phoneNumber','facebook','instagram','website','email')

    def is_valid(self):
        super(ContactSerializer, self).is_valid()
        try:
            phoneNumber=int(self.data['phoneNumber'])
        except :
            return False
        return True


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields='__all__'
        extra_kwargs={
            'id':{'read_only':True}
        }

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feature
        fields=('feature',)

class ResturantSerializer(serializers.ModelSerializer):
    address=AddressSerializer(many=False,read_only=True)
    reviews=ReviewSerializer(many=True,read_only=True)
    contact=ContactSerializer(many=False,read_only=True)
    images=ImageSerializer(many=True,read_only=True)
    menus=MenuSerializer(many=True,read_only=True)
    features=FeatureSerializer(many=True,read_only=True)
    class Meta:
        model=Resturant
        fields=('id','name','description','open_time','close_time','delivery_available','cover_photo','address','images','features','menus','contact','reviews')
        extra_kwargs={
            'id':{'read_only':True}
        }

class ResturantCUSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturant
        fields = ('name','description','open_time','close_time','delivery_available','cover_photo')



