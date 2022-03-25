from django.urls import path
from . import views
app_name='mykart'
urlpatterns = [
    path('', views.allProducts, name='allProducts'),
    path('<slug:c_slug>/', views.allProducts, name='ProductsByCategories'),
    path('<slug:c_slug>/<slug:product_slug>', views.productDetail, name='ProductDetails'),
]