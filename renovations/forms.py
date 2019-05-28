from django.forms import ModelForm, Textarea
from renovations.models import Product


class NewProductForm(ModelForm):
    class Meta:
        model = Product
        widgets = {
            "description": Textarea(attrs={'rows': 5, 'cols': 20})
        }
        exclude = []

