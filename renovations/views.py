from django.shortcuts import render
from django.views.generic import ListView
from renovations.models import Product


# Create your views here.
class AllProducts(ListView):
    model = Product
