from django.urls import path
from .views import (
    CardListView,
    CardDeleteView,
    CardCreateView,
    CardUpdateView,
    CardDetailView,
)

urlpatterns = [
    path("", CardListView.as_view(), name="card_list"),
    path("detail/<int:pk>/", CardDetailView.as_view(), name="card_detail"),
    path("new/", CardCreateView.as_view(), name="card_create"),
    path("<int:pk>/edit", CardUpdateView.as_view(), name="card_update"),
    path("<int:pk>/delete", CardDeleteView.as_view(), name="card_delete"),
]
