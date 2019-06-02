from django.forms import ModelForm, Textarea, NumberInput
from renovations.models import Product, Room, Renovation


class NewProductForm(ModelForm):
    class Meta:
        model = Product
        widgets = {
            "description": Textarea(attrs={'rows': 5, 'cols': 20})
        }
        exclude = []


class NewRoomForm(ModelForm):
    class Meta:
        model = Room
        widgets = {
            "description": Textarea(attrs={'rows': 5, 'cols': 20}),
            "width": NumberInput(attrs={'style': 'width:7em'}),
            "length": NumberInput(attrs={'style': 'width:7em'}),
            "height": NumberInput(attrs={'style': 'width:7em'}),
            "tiles_height": NumberInput(attrs={'style': 'width:7em'}),
        }
        exclude = []


class NewRenovationForm(ModelForm):
    class Meta:
        model = Renovation
        widgets = {
            "description": Textarea(attrs={'rows': 5, 'cols': 20})
        }
        exclude = []
