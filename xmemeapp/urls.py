from django.urls import path, include
from .views import homeView, editView
from . import views

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('edit/<int:pk>/', editView.as_view(), name='edit'),
    path('remove/<int:pk>/', views.deletePost, name='delete'),
    path('.well-known/pki-validation/B49196DA6EF9213ADBB45726509F1A97.txt/', views.sllAuth)
]