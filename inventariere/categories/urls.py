from django.urls import path
from categories import views
from categories.views import DeleteCategoryView

app_name = 'categories'

urlpatterns = [
    path('adaugare/', views.CreateCategoryView.as_view(), name='adaugare_categorie'),
    path('', views.CategoriesView.as_view(), name='lista_categorii'),
    path('<int:pk>/delete/', DeleteCategoryView.as_view(), name='delete_category'),
]
