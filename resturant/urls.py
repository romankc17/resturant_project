from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('resturants',views.ResturantListView)
# router.register('addresses',views.AddressView)
# router.register('menus',views.MenuView)
# router.register('item_types',views.ItemTypeView)
router.register('images',views.ImagesView)

urlpatterns = [
    path('all_',include(router.urls)),
    path('',views.ResturantListView.as_view())
]
