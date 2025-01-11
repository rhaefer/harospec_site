from django.contrib import admin
from django.urls import path, include  # Use `include` to connect to app-level URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('harospec_site.urls')),  # Include URLs from the app
]