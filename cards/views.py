from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Card
from django.urls import reverse_lazy

# Create your views here.
class CardListView(ListView):
    template_name = "cards/card-list.html"
    model = Card


class CardDetailView(DetailView):
    template_name = "cards/card-detail.html"
    model = Card


class CardCreateView(CreateView):
    template_name = "cards/card-create.html"
    model = Card
    fields = ["title", "author", "body"]


class CardUpdateView(UpdateView):
    template_name = "cards/card-update.html"
    model = Card
    fields = ["title", "author", "body"]


class CardDeleteView(DeleteView):
    template_name = "cards/card-delete.html"
    model = Card
    success_url = reverse_lazy("list")
