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
            "width": NumberInput(attrs={'style': 'width:5em'}),
            "length": NumberInput(attrs={'style': 'width:5em'}),
            "height": NumberInput(attrs={'style': 'width:5em'}),
            "tiles_height": NumberInput(attrs={'style': 'width:5em'}),
        }
        exclude = []


class NewRenovationForm(ModelForm):
    class Meta:
        model = Renovation
        widgets = {
            "description": Textarea(attrs={'rows': 5, 'cols': 20})
        }
        exclude = []
