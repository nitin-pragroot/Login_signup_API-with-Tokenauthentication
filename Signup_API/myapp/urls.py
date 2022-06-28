from django.contrib import admin
from .import views
from django.urls import path

urlpatterns = [
path('registrationlist/',views.RegistrationList.as_view()),
path('registrationDetail/<int:pk>/', views.RegisterDetails.as_view()),
path('search/', views.SearchListView.as_view()),
 
]