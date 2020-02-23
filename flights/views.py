from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from datetime import datetime
from .serializers import FlightSerializer, BookingSerializer

class Flights (ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class Bookings (ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.today())
    serializer_class = BookingSerializer
