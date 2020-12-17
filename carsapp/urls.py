from django.contrib import admin
from django.urls import path, include

from carsapp import views

urlpatterns = [
    path('api/new-cars/', views.CarDetails.as_view(), name='new-cars'),
    path('api/car-list/<int:pk>/', views.CarList.as_view()),
]