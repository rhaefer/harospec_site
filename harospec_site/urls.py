from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('services/', views.services, name='services'),  # Services subpage
    path('portfolio/', views.portfolio, name='portfolio'),  # Portfolio subpage
    path('contact/', views.contact, name='contact'),  # Contact subpage
    path('project1/', views.project1, name='project1'),
    path('project2/', views.project2, name='project2'),
    path('project3/', views.project3, name='project3'),
]