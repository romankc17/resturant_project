from django.http.response import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Resturant,Address,Menu,ItemType,Images
from .serializers import ResturantSerializer, ImageSerializer


class ResturantListView(generics.ListAPIView):
    queryset=Resturant.objects.all()
    serializer_class=ResturantSerializer

class ImagesView(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

class ResturantView(APIView):
    serializer_class=ResturantSerializer

    def get(self,request,id,format=None):
        r=Resturant.objects.get(id=id)
        images=r.images_set