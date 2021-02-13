from django.urls import path, include
from .views import homeView, editView

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('edit/<int:pk>/', editView.as_view(), name='edit')
]