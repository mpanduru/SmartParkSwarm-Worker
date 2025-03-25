from django.urls import path
from .views import ParkingLotList, ParkingSpotList, ParkingSpotDetail, VehicleEntryList, VehicleEntryDetail

urlpatterns = [
    # path('ParkingLot/', ParkingLotInsert.as_view()),
    path('ParkingLot/', ParkingLotList.as_view()),
    path('ParkingSpot/', ParkingSpotList.as_view()),
    path('ParkingSpot/<uuid:pk>/', ParkingSpotDetail.as_view()),
    path('VehiceEntry/', VehicleEntryList.as_view()),
    path('VehiceEntry/<uuid:pk>/', VehicleEntryDetail.as_view()),
]