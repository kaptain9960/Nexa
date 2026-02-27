from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('service-details/', views.service_details, name='service-details'),
    path('download_resume/', views.download_resume, name='download_resume'),
    path('about/', views.about, name="about"),
]
