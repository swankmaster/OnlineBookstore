from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(CartHasInventoryBook)
admin.site.register(Order)
admin.site.register(OrderedBook)
admin.site.register(PaymentCard)
admin.site.register(ShippingAddress)
admin.site.register(Promotion)
admin.site.register(Transaction)
admin.site.register(User1)

