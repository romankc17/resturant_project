from django.urls import path
from . import views

urlpatterns = [
    path('',views.ResturantListView.as_view()),
    path('r/<int:id>/',views.ResturantDetailView.as_view()),
    path('r/',views.ResturantCUView.as_view()),
    path('address/',views.AddressView.as_view()),
    path('contact/',views.ContactView.as_view()),
    # path('feature/',views.FeatureView.as_view()),
]
