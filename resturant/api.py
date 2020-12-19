from django.http.response import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Resturant,Address,Menu,ItemType,Images
from .serializers import ResturantSerializer,AddressSerializer,MenuSerializer,ItemTypeSerializer,ImagesSerializer

class ResturantView(viewsets.ModelViewSet):
    queryset = Resturant.objects.all()
    serializer_class = ResturantSerializer

class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class ItemTypeView(viewsets.ModelViewSet):
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer

class ImagesView(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

