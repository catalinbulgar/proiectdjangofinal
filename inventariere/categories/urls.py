from django.urls import path
from categories import views

app_name = 'categories'

urlpatterns = [
    path('adaugare/', views.CreateCategoryView.as_view(), name='adaugare_categorie'),
    path('', views.CategoriesView.as_view(), name='lista_categorii')
]
