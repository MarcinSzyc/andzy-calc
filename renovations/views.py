from django.views.generic import ListView, View
from renovations.models import Renovation, Product, Room, Cost, PRODUCT_TYPE, ROOM_TYPE
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, reverse, render
from django.contrib import messages
from renovations.forms import NewRoomForm, NewRenovationForm, NewCostForm
from functools import reduce
import xlsxwriter
import io
from django.http.response import HttpResponse
from renovations.excel_utils import renovation_summary, renovation_room_cost


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


class RoomNew(View):

    def post(self, request):
        filled_form = NewRoomForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            new_cost = Cost.objects.create()
            new_room = Room.objects.last()
            new_room.cost = new_cost
            new_room.save()
            messages.success(request, 'Room created successfully!!!')
        else:
            error_list = [item for item in filled_form.errors.values()]
            messages.error(request, f'Upps, something went wrong!!! \n {error_list}')
        return redirect(self.request.META.get('HTTP_REFERER'))

    success_message = 'BOOM! Room updated successfully!!'


class RoomUpdate(View):
    template = 'renovations/edit_room.html'

    def get(self, request, pk):
        product = Product.objects.all()
        product_type = PRODUCT_TYPE
        room = Room.objects.get(pk=pk)
        new_room_form = NewRoomForm(instance=room)
        cost = room.cost
        new_cost_form = NewCostForm(instance=cost)
        return render(request, self.template, locals())

    def post(self, request, pk):
        room_instance = Room.objects.get(pk=pk)
        filled_form = NewRoomForm(request.POST, instance=room_instance)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Room updated successfully!!!')
        else:
            error_list = [item for item in filled_form.errors.values()]
            messages.error(request, f'Upps, something went wrong!!! \n {error_list}')
        return redirect(self.request.META.get('HTTP_REFERER'))


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ROOM_TYPE'] = ROOM_TYPE
        return context


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
        context['ROOM_TYPE'] = ROOM_TYPE
        context['total_cost'] = round(
            reduce((lambda x, y: x + y), [room.cost.total_sum for room in Renovation.objects.get(
                pk=self.kwargs['pk']).room_set.all()]), 2)
        return context

    success_message = 'BOOM! Renovation updated successfully!!'


class RenovationDelete(View):

    def get(self, request, pk):
        renovation_instance = Renovation.objects.get(pk=pk)
        renovation_instance.delete()
        messages.error(request, "BOOM! Renovation deleted successfully")
        return redirect('renovations:all-renovations')


class CostUpdate(View):
    template = 'renovations/edit_room.html'

    def get(self, request, pk):
        product = Product.objects.all()
        product_type = PRODUCT_TYPE
        room_instance = Room.objects.get(pk)
        new_room_form = NewRoomForm(instance=room_instance)
        cost = Cost.objects.get(room_id=pk)
        return render(request, self.template, locals())

    def post(self, request, pk):
        cost_instance = Cost.objects.get(pk=pk)
        filled_form = NewCostForm(request.POST, instance=cost_instance)
        for item in request.POST:
            print(item)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Cost updated successfully!!!')
        else:
            error_list = [item for item in filled_form.errors.values()]
            messages.error(request, f'Upps, something went wrong!!! \n {error_list}')
        return redirect(self.request.META.get('HTTP_REFERER'))


class Excel(View):
    def get(self, request, pk):
        output = io.BytesIO()

        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        renovation_worksheet = workbook.add_worksheet('renovation')
        renovation_summary(renovation_worksheet, workbook, pk)
        renovation_room_cost(renovation_worksheet, workbook, pk)
        workbook.close()

        output.seek(0)
        response = HttpResponse(output.read(),
                                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = "attachment; filename=Renovation.xlsx"
        output.close()

        return response
