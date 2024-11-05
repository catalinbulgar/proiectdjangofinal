from django.urls import path
from inventory import views
from inventory.views import DeleteProductView

app_name = 'inventory'

urlpatterns = [
    path('', views.AllProducts.as_view(), name='listare_produse'),
    path('adaugare_produs/', views.CreateNewProduct.as_view(), name='adaugare_produs'),
    path('<int:pk>/modificare', views.UpdateProduct.as_view(), name='modifica'),
    path('sterge/<int:pk>/', DeleteProductView.as_view(), name='sterge'),
]
