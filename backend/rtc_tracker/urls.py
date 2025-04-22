from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Define the home view that will be rendered for the root path
def home(request):
    return render(request, 'home.html')  # Render the home page using the 'home.html' template

# Define URL patterns for the main application
urlpatterns = [
    path('', home),  # Root path points to the home view
    path('admin/', admin.site.urls),  # Admin interface path
    path('api/', include('rtc_app.urls')),  # Include API paths from rtc_app
]
