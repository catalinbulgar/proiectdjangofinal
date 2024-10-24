from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from inventory.models import Product


class CreateNewProduct(LoginRequiredMixin, CreateView):

    model = Product
    template_name = 'forms.html'
    fields = ['name', 'description', 'category', 'quantity', 'price_per_unit']

    def get_success_url(self):
        return reverse('inventory:adaugare_produs')


class AllProducts(LoginRequiredMixin, ListView):

    model = Product
    template_name = 'inventory/inventory_index.html'


class UpdateProduct(LoginRequiredMixin, UpdateView):

    model = Product
    fields = ['name', 'description', 'category', 'quantity', 'price_per_unit']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('inventory:listare_produse')