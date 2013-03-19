from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __unicode__(self):
        # preferred string formatting, look at: PEP-3101
        data = {'name': self.name, 'details': self.details}
        return u'Name: {name}; Details: {details}'.format(**data)
