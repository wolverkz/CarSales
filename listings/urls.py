from django.urls import path
from .views import CarListView, CarRetrieveUpdateDeleteView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarRetrieveUpdateDeleteView.as_view(), name='car-detail'),
]