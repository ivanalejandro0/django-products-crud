from django.shortcuts import render_to_response
from django.template import RequestContext

from products.forms import ProductForm


def add(request):
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()

    content = {'title': 'Add new product', 'form': form}
    context_instance = RequestContext(request)
    return render_to_response('products/form.html', content, context_instance)
