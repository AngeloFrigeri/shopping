from django.urls import path

from ecommerce import views

urlpatterns = [
    path('computeShipping/<sell>/', views.ComputeShipping.as_view()),
]
