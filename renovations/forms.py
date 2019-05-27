from django.forms import ModelForm
from renovations.models import Product


class NewProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = []
