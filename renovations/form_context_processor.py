from renovations.forms import NewProductForm, NewRoomForm, NewRenovationForm, NewCostForm


def renovations_form_context(request):
    result = {
        'new_product_form': NewProductForm,
        'new_room_form': NewRoomForm,
        'new_renovation_form': NewRenovationForm,
        'new_cost_form': NewCostForm
    }
    return result
