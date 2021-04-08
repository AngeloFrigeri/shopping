from django.urls import path

from ecommerce import views

urlpatterns = [
    path('computeShipping/<sell_id>/', views.ComputeShipping.as_view()),
    path('', views.ProductsListing.as_view()),
    path('cart/<sell_id>/', views.CartUpdate.as_view()),
]
