from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView

from categories.models import Category
from inventory.models import Product


class CreateNewProduct(LoginRequiredMixin, CreateView):

    model = Product
    template_name = 'forms.html'
    fields = ['name', 'description', 'category', 'quantity', 'price_per_unit']

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        if Product.objects.filter(name__iexact=name).exists():
            messages.error(self.request, 'Produsul deja existent')
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inventory:listare_produse')


class AllProducts(LoginRequiredMixin, ListView):

    model = Product
    template_name = 'inventory/inventory_index.html'
    context_object_name = 'product_list'


class UpdateProduct(LoginRequiredMixin, UpdateView):

    model = Product
    fields = ['name', 'description', 'category', 'quantity', 'price_per_unit']
    template_name = 'forms.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inventory:listare_produse')


class DeleteProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('inventory:listare_produse')


class SomeView(LoginRequiredMixin, TemplateView):
    template_name = 'forms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
