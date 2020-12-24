from django.http.response import JsonResponse
from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (Resturant, Address, Menu, ItemType, Images, Contact, Feature)
from .serializers import (ResturantSerializer,
                          ImageSerializer,
                          ResturantCUSerializer,
                          AddressSerializer, ContactSerializer, FeatureSerializer)


class ResturantListView(generics.ListAPIView):
    queryset=Resturant.objects.all()
    serializer_class=ResturantSerializer

class ResturantUpdateView(generics.UpdateAPIView):
    # queryset=Resturant.objects.all()
    serializer_class=ResturantSerializer

    def update(self, request,id, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class ImagesView(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

class ResturantDetailView(APIView):
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
class IsStaffUser(BasePermission):
    def has_permission(self,request,view):
        return request.user and request.user.is_staff

class ResturantCUView(APIView):
    serializer_class=ResturantCUSerializer
    permission_classes = (IsStaffUser,)

    def post(self,request):
        queryset = Resturant.objects.filter(user=request.user)
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            print('valid')
            name = serializers.data.get('name')
            description = serializers.data.get('description')
            open_time = serializers.data.get('open_time')
            close_time = serializers.data.get('close_time')
            delivery_available = serializers.data.get('delivery_available')
            cover_photo = request.data['cover_photo']

            if not queryset.exists():
                resturant = Resturant(
                    user=request.user,
                    name=name,
                    description=description,
                    open_time=open_time,
                    close_time = close_time,
                    delivery_available=delivery_available,
                    cover_photo=cover_photo,
                )
                resturant.save()
            else:
                resturant = queryset[0]
                resturant.user=request.user
                resturant.name = name
                resturant.description = description
                resturant.open_time = open_time
                resturant.close_time = close_time
                resturant.delivery_available = delivery_available
                resturant.cover_photo = cover_photo

                resturant.save(update_fields=['user','name', 'description', 'open_time',
                                              'close_time', 'delivery_available', 'cover_photo'])
            return Response(ResturantSerializer(resturant).data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Resturant could not be created with received data.'
            }, status=status.HTTP_400_BAD_REQUEST)

class AddressView(APIView):
    serializer_class=AddressSerializer
    permission_classes = (IsStaffUser,)

    def post(self,request):
        queryset = Resturant.objects.filter(user=request.user)
        if not queryset.exists():
            return Response(
                {'Bad Request':'Resturant Doesn\'t Exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        resturant = queryset[0]
        address=queryset[0].address
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            district = serializers.data.get('district')
            province = serializers.data.get('province')
            city = serializers.data.get('city')
            tole = serializers.data.get('tole')
            if not address:
                address = Address(
                    district=district,
                    province=province,
                    city=city,
                    tole =tole,
                )
                address.save()
                resturant.address=address
                resturant.save()
            else:
                address.district = district
                address.province = province
                address.city = city
                address.tole = tole
                address.save(update_fields=['district','province','city','tole'])
            return Response(AddressSerializer(address).data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Address could not be created with received data.'
            }, status=status.HTTP_400_BAD_REQUEST)

class ContactView(APIView):
    serializer_class=ContactSerializer
    permission_classes = (IsStaffUser,)

    def post(self,request):
        queryset = Resturant.objects.filter(user=request.user)
        if not queryset.exists():
            return Response(
                {'Bad Request':'Resturant Doesn\'t Exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        resturant = queryset[0]
        contact=queryset[0].contact
        # print(request.data)
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            phoneNumber = serializers.data.get('phoneNumber')
            facebook = serializers.data.get('facebook')
            instagram = serializers.data.get('instagram')
            email = serializers.data.get('email')
            website = serializers.data.get('website')
            if not contact:
                contact = Contact(
                    phoneNumber=phoneNumber,
                    facebook=facebook,
                    instagram=instagram,
                    email =email,
                    website =website,
                )
                contact.save()
                resturant.contact=contact
                resturant.save()
            else:
                contact.phoneNumber = phoneNumber
                contact.facebook = facebook
                contact.instagram = instagram
                contact.email = email
                contact.website = website
                contact.save(update_fields=['phoneNumber','facebook','instagram','email','website'])
            return Response(ContactSerializer(contact).data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Contact could not be created with received data.'
            }, status=status.HTTP_400_BAD_REQUEST)

# class FeatureView(APIView):
#     serializer_class=FeatureSerializer
#     permission_classes = (IsStaffUser,)
#
#     def post(self,request):
#         queryset = Resturant.objects.filter(user=request.user)
#         if not queryset.exists():
#             return Response(
#                 {'Bad Request':'Resturant Doesn\'t Exist.'},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#
#         resturant = queryset[0]
#         feature=queryset[0].contact
#         serializers=self.serializer_class(data=request.data,many=True)
#         print(serializers)
#         if serializers.is_valid():
#             features = serializers.data.get('feature')
#             if not feature:
#                 feature = Feature(
#                     feature=feature,
#                 )
#                 feature.resturant=resturant
#                 feature.save()
#             else:
#                 feature.feature = features
#                 feature.save(update_fields=['feature',])
#             return Response(FeatureSerializer(feature).data, status=status.HTTP_201_CREATED)
#
#         return Response({
#             'status': 'Bad request',
#             'message': 'Feature could not be created with received data.'
#             }, status=status.HTTP_400_BAD_REQUEST)


