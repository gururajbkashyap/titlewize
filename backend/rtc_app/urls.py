from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RTCRecordViewSet, scrape_rtc_view  # Ensure views are correctly imported

# Create a router and register the viewset with it
router = DefaultRouter()
router.register(r'rtc-records', RTCRecordViewSet)

# Define URL patterns, including custom scrape route
urlpatterns = router.urls + [
    path('scrape/<int:year>/', scrape_rtc_view, name='scrape_rtc'),
]
