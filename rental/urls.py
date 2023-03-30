from django.contrib import admin
from django.urls import path, include
from ApRental import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('searchbyFilter/', views.searchByF ,name='filter'),
    path('searchbyMap/', views.searchByM ,name='map'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calculator/', views.calc, name='calc'),
    path('login/', views.login, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
