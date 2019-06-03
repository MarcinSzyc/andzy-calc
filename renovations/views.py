from django.views.generic import ListView, View, DetailView
from renovations.models import Product, Room, Renovation, PRODUCT_TYPE, ROOM_TYPE
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib import messages
from renovations.forms import NewRoomForm


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
    fields = '__all__'
    template_name = 'renovations/products_view.html'
    success_url = reverse_lazy('renovations:all-products')
    success_message = 'BOOM! Product created successfully!!'


class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('renovations:all-products')
    success_message = 'BOOM! Product updated successfully!!'


class ProductDelete(View):

    def get(self, request, pk):
        product_instance = Product.objects.get(pk=pk)
        product_instance.delete()
        messages.error(request, "BOOM! Product deleted successfully")
        return redirect('renovations:all-products')


class AllRooms(ListView):
    model = Room
    template_name = 'renovations/room_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        # context['new_product_form'] = NewProductForm
        context['ROOM_TYPE'] = ROOM_TYPE
        return context


class EditRoom(UpdateView):
    form_class = NewRoomForm
    template_name = 'renovations/edit_room.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['ROOM_TYPE'] = ROOM_TYPE
        return context



class RoomNew(SuccessMessageMixin, CreateView):
    model = Room
    fields = '__all__'
    template_name = 'renovations/products_view.html'
    success_url = reverse_lazy('renovations:all-rooms')
    success_message = 'BOOM! Room created successfully!!'


class RoomUpdate(SuccessMessageMixin, UpdateView):
    model = Room
    form_class = NewRoomForm
    template_name = 'renovations/edit_room.html'
    success_url = reverse_lazy('renovations:all-rooms')
    success_message = 'BOOM! Room updated successfully!!'


class RoomDelete(View):

    def get(self, request, pk):
        room_instance = Room.objects.get(pk=pk)
        room_instance.delete()
        messages.error(request, "BOOM! Room deleted successfully")
        return redirect('renovations:all-rooms')
