# rtc_app/serializers.py
from rest_framework import serializers
from .models import RTCRecord

class RTCRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RTCRecord
        fields = '__all__'
