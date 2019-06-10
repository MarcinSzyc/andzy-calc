from django.views.generic import ListView, View
from renovations.models import Renovation, Product, Room, PRODUCT_TYPE, ROOM_TYPE
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, reverse, render
from django.contrib import messages
from renovations.forms import NewRoomForm, NewRenovationForm


class AllProducts(ListView):
    model = Product
    template_name = 'renovations/list_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PRODUCT_TYPE'] = PRODUCT_TYPE
        return context


class ProductNew(SuccessMessageMixin, CreateView):
    model = Product
    fields = '__all__'
    # template_name = 'renovations/products_view.html'
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
    template_name = 'renovations/list_room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ROOM_TYPE'] = ROOM_TYPE
        return context


class RoomNew(SuccessMessageMixin, CreateView):
    model = Room
    fields = '__all__'
    # template_name = 'renovations/products_view.html'
    success_url = reverse_lazy('renovations:all-rooms')
    success_message = 'BOOM! Room created successfully!!'


class RoomUpdate(SuccessMessageMixin, UpdateView):
    model = Room
    form_class = NewRoomForm
    template_name = 'renovations/edit_room.html'

    def get_success_url(self):
        return reverse('renovations:update-room', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PRODUCT_TYPE'] = PRODUCT_TYPE
        return context

    success_message = 'BOOM! Room updated successfully!!'


class RoomDelete(View):

    def get(self, request, pk):
        room_instance = Room.objects.get(pk=pk)
        room_instance.delete()
        messages.error(request, "BOOM! Room deleted successfully")
        return redirect('renovations:all-rooms')


class AddProductView(View):
    template = 'renovations/add_product_to_room_view.html'

    def get(self, request, room_id):
        room_instance = Room.objects.get(pk=room_id)
        all_products = Product.objects.all()
        product_type = PRODUCT_TYPE
        return render(request, self.template, locals())


class AddProductToRoom(View):
    template = 'renovations/add_product_to_room_view.html'

    def get(self, request, room_id, product_id):
        room_instance = Room.objects.get(pk=room_id)
        product_instance = Product.objects.get(pk=product_id)
        room_instance.product.add(product_instance)
        messages.success(request, "Product added!")
        return redirect('renovations:add-product-view', room_id)


class RemoveProductFromRoom(View):
    template = 'renovations/add_product_to_room_view.html'

    def get(self, request, room_id, product_id):
        room_instance = Room.objects.get(pk=room_id)
        product_instance = Product.objects.get(pk=product_id)
        messages.error(request, "Product removed!")
        room_instance.product.remove(product_instance)
        return redirect('renovations:add-product-view', room_id)


class AllRenovations(ListView):
    model = Renovation
    template_name = 'renovations/list_renovation.html'


class RenovationAdd(SuccessMessageMixin, CreateView):
    model = Renovation
    fields = '__all__'
    success_url = reverse_lazy('renovations:all-renovations')
    success_message = 'BOOM! Renovation created successfully!!'


class RenovationUpdate(SuccessMessageMixin, UpdateView):
    model = Renovation
    form_class = NewRenovationForm
    template_name = 'renovations/edit_renovation.html'

    def get_success_url(self):
        return reverse('renovations:update-renovation', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    success_message = 'BOOM! Room updated successfully!!'


class RenovationDelete(View):

    def get(self, request, pk):
        renovation_instance = Renovation.objects.get(pk=pk)
        renovation_instance.delete()
        messages.error(request, "BOOM! Renovation deleted successfully")
        return redirect('renovations:all-renovations')
