from renovations.forms import NewProductForm



def product_form_context(request):
    result = {
        'new_product_form': NewProductForm
    }
    return result