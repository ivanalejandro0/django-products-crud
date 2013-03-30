from django.conf.urls import patterns, url
from django.views.generic import ListView
from products.models import Product

urlpatterns = patterns('products.views',
    url(r'^list/$', ListView.as_view(
        template_name="products/list.html",
        model=Product), name='list'),
    url(r'^add/$', 'add_or_edit', name='add'),
    url(r'^edit/(?P<id>\d+)/$', 'add_or_edit', name='edit'),
    url(r'^remove/(?P<id>\d+)/$', 'remove', name='remove'),
)
