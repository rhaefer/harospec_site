from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('services/', views.services, name='services'),  # Services subpage
    path('portfolio/', views.portfolio, name='portfolio'),  # Portfolio subpage
    path('contact/', views.contact, name='contact'),  # Contact subpage
]