# rtc_app/models.py
from django.db import models

class RTCRecord(models.Model):
    district = models.CharField(max_length=100)
    taluk = models.CharField(max_length=100)
    hobli = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    survey_no = models.CharField(max_length=50)
    hissa_no = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    date_fetched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"RTC for {self.survey_no} in {self.village} for year {self.year}"
