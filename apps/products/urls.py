from django.conf.urls import patterns, url
from django.views.generic import ListView
from products.models import Product

urlpatterns = patterns('products.views',
    url(r'^list/$', ListView.as_view(
        template_name="products/list.html",
        model=Product), name='products_list'),
    url(r'^add/$', 'add', name='product_add'),
    url(r'^edit/(?P<id>\d+)/$', 'edit', name='product_edit'),
    url(r'^remove/(?P<id>\d+)/$', 'remove', name='product_remove'),
)
