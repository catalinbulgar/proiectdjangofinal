from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from categories.forms import CategoryForm
from categories.models import Category


class CreateCategoryView(LoginRequiredMixin, CreateView):

    model = Category
    form_class = CategoryForm
    template_name = 'categories/create_category.html'

    def get_success_url(self):
        return reverse('categories:lista_categorii')


class CategoriesView(LoginRequiredMixin, ListView):

    model = Category
    template_name = 'categories/categories_index.html'
    context_object_name = 'inventory_list'


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/delete_category.html'
    context_object_name = 'category'

    def get_success_url(self):
        return reverse_lazy('categories:lista_categorii')
