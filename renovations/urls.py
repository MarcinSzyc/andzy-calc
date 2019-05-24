from django.urls import path
from renovations.views import AllProducts

app_name = "renovations"

urlpatterns = [
    path('products/', AllProducts.as_view(), name='all-products'),
]
