from django.contrib import admin
from .models import Like, Product, CustomUser, Cart, Comment, Order

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Like)
admin.site.register(CustomUser)
admin.site.register(Comment)
admin.site.register(Cart)
