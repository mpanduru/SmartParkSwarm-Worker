from rest_framework import generics
from .models import ParkingLot, ParkingSpot, VehicleEntry
from .serializers import ParkingLotSerializer, ParkingSpotSerializer, VehicleEntrySerializer

class ParkingLotCreate(generics.CreateAPIView):
    serializer_class = ParkingLotSerializer
    queryset = ParkingLot.objects.all()

class ParkingLotDetail(generics.RetrieveAPIView):
    serializer_class = ParkingLotSerializer
    queryset = ParkingLot.objects.all()

class ParkingLotList(generics.ListCreateAPIView):
    serializer_class = ParkingLotSerializer
    queryset = ParkingLot.objects.all()

class ParkingLotDetail(generics.RetrieveAPIView):
    serializer_class = ParkingLotSerializer
    queryset = ParkingLot.objects.all()

class ParkingSpotList(generics.ListCreateAPIView):
    serializer_class = ParkingSpotSerializer

    def get_queryset(self):
        queryset = ParkingSpot.objects.all()
        parkinglot = self.request.query_params.get('parkinglot')
        if parkinglot is not None:
            queryset = queryset.filter(lot_uuid=parkinglot)
        return queryset
    
class ParkingSpotDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParkingSpotSerializer
    queryset = ParkingSpot.objects.all()

class VehicleEntryList(generics.ListCreateAPIView):
    serializer_class = VehicleEntrySerializer

    def get_queryset(self):
        queryset = VehicleEntry.objects.all()
        parkingspot = self.request.query_params.get('parkingspot')
        if parkingspot is not None:
            queryset = queryset.filter(spot_id=parkingspot)
        return queryset
    
class VehicleEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleEntrySerializer
    queryset = VehicleEntry.objects.all()