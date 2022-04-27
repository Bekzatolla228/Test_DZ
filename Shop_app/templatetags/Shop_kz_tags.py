from django import template
from Shop_app.models import *

register = template.Library()

@register.inclusion_tag('Shop_app/products.html')
def show_products():
    products = Product.objects.all()
    return {'products': products}