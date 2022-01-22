from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo, Product, Seller, Customer, Sales, Purchase

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

#########################Dashboard###################################
class ProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = ('product_id', 'product_type', 'product_name','product_rate')

class SellerForm(forms.ModelForm):
    class Meta():
        model = Seller
        fields = ('seller_id', 'seller_name', 'seller_number', 'seller_address')

class CustomerForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields = ('customer_id', 'customer_name', 'customer_number', 'customer_address')

class SalesForm(forms.ModelForm):
    class Meta():
        model = Sales
        fields = ('seller_id', 'product_id', 'sales_date', 'sales_qty')


class PurchaseForm(forms.ModelForm):
    class Meta():
        model = Purchase
        fields = ('customer_id', 'product_id', 'purchase_date', 'purchase_qty')
