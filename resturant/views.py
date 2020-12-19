from django.http.response import JsonResponse
from rest_framework import generics, viewsets, status
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
        queryset=Resturant.objects.filter(id=id)
        if queryset.exists():
            resturant=queryset[0]
            data=ResturantSerializer(resturant).data
            for m in resturant.menus.all():
                l=list(filter(lambda c : c['id'] == m.id, data['menus']))
                if l:
                    print(l)
                    l[0]['item_type']=m.item_type.type

            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({'Resturant Not Found': 'Invalid Resturant id.'},
                            status=status.HTTP_404_NOT_FOUND)