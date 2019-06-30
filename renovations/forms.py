from django.forms import ModelForm, Textarea, NumberInput, Select
from renovations.models import Product, Room, Renovation, Cost
from django import forms


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


class NewCostForm(ModelForm):
    class Meta:
        model = Cost
        widgets = {
            "floor": NumberInput(attrs={'class': 'floor-cost to-sum'}),
            "walls": NumberInput(attrs={'class': 'walls-cost to-sum'}),
            "ceiling": NumberInput(attrs={'class': 'ceiling-cost to-sum'}),
            "tiles": NumberInput(attrs={'class': 'tiles-cost to-sum'}),
            "addons": NumberInput(attrs={'class': 'addon-cost to-sum'}),
            "basic_sum": NumberInput(attrs={'class': 'sum-cost to-total'}),
            "labor": NumberInput(attrs={'class': 'labor-cost to-total'}),
            "total_sum": NumberInput(attrs={'class': 'total-cost'})
        }
        exclude = []


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)
