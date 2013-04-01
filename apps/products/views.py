from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from products.forms import ProductForm
from products.models import Product

def add(request):
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

            # If the save was successful, redirect to another page
            redirect_url = reverse('products:list')
            return HttpResponseRedirect(redirect_url)
    else:
        form = ProductForm()

    content = {'title': 'Add new product', 'form': form}
    context_instance = RequestContext(request)
    return render_to_response('products/form.html', content, context_instance)


# look at: http://stackoverflow.com/questions/1854237/django-edit-form-based-on-add-form
def add_or_edit(request, id=None):
    if id:
        product = get_object_or_404(Product, pk=id)
        action = "Edit "
    else:
        product = Product()
        action = "Add a new "

    if request.POST:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()

            # If the save was successful, redirect to another page
            redirect_url = reverse('products:list')
            return HttpResponseRedirect(redirect_url)
    else:
        form = ProductForm(instance=product)

    content = {'title': action + 'product', 'form': form}
    context_instance = RequestContext(request)
    return render_to_response('products/form.html', content, context_instance)


def remove(request, id=None):
    # TODO: not implemented yet, redirect to list
    messages.add_message(request, messages.SUCCESS, "The item was succesfuly removed")
    redirect_url = reverse('products:list')
    return HttpResponseRedirect(redirect_url)
