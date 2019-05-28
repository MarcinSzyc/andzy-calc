from django.views.generic import ListView, View
from renovations.models import Product, PRODUCT_TYPE
from django.views.generic.edit import CreateView, UpdateView, BaseDeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib import messages
from renovations.forms import NewProductForm


class AllProducts(ListView):
    model = Product
    template_name = 'renovations/product_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        # context['new_product_form'] = NewProductForm
        context['PRODUCT_TYPE'] = PRODUCT_TYPE
        return context


class ProductNew(SuccessMessageMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'type']
    template_name = 'renovations/products_view.html'
    success_url = reverse_lazy('renovations:all-products')
    success_message = 'BOOM! Product created successfully!!'


class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'type']
    success_url = reverse_lazy('renovations:all-products')
    success_message = 'BOOM! Product updated successfully!!'


class ProductDelete(View):

    def get(self, request, pk):
        product_instance = Product.objects.get(pk=pk)
        product_instance.delete()
        messages.error(request, "BOOM! Product deleted successfully")
        return redirect('renovations:all-products')
