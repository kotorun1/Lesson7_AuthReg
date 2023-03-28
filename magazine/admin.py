from django.contrib import admin
from .models import Manufacturer, Country, Product, Cart, Order
# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Country)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)

