from django.urls import path, include
from .views import homeView, editView
from . import views

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('edit/<int:pk>/', editView.as_view(), name='edit'),
    path('remove/<int:pk>/', views.deletePost, name='delete'),
    path('.well-known/pki-validation/D55B041A6A8319F89D4ACC6E48258485.txt/', views.sllAuth)
]