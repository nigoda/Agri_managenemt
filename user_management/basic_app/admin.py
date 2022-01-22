from django.contrib import admin
from basic_app.models import UserProfileInfo, Product, Seller, Customer, Sales, Purchase

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(Sales)
admin.site.register(Purchase)
