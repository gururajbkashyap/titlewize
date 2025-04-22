from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import RTCRecord
from .serializers import RTCRecordSerializer
from .scraper import fetch_rtc  # ✅ Make sure scraper.py is in the same app folder

class RTCRecordViewSet(viewsets.ModelViewSet):
    queryset = RTCRecord.objects.all()
    serializer_class = RTCRecordSerializer

@api_view(['GET'])
def scrape_rtc_view(request, year):
    try:
        fetch_rtc(year)
        return Response({"message": f"RTC for {year} fetched successfully."})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
