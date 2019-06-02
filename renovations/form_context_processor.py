from renovations.forms import NewProductForm, NewRoomForm



def renovations_form_context(request):
    result = {
        'new_product_form': NewProductForm,
        'new_room_form': NewRoomForm
    }
    return result