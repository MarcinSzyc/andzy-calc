from renovations.forms import NewProductForm, NewRoomForm, NewRenovationForm, NewCostForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, UserCreationForm


def renovations_form_context(request):
    result = {
        'new_product_form': NewProductForm,
        'new_room_form': NewRoomForm,
        'new_renovation_form': NewRenovationForm,
        'new_cost_form': NewCostForm,
        'authentication_form': AuthenticationForm,
        'password_reset_form': PasswordResetForm,
        'registration_form': UserCreationForm
    }
    return result
