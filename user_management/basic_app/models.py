from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):


    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #Additional
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)


    def __str__(self):
        return self.user.username


############################Dashboard#####################################

class Product(models.Model):
    product_id = models.CharField(max_length=256,unique=True)
    product_type = models.CharField(max_length=256)
    product_name = models.CharField(max_length=256)
    product_rate = models.CharField(max_length=256)

    objects = models.Manager()


    def __str__(self):
        return self.product_id


class Seller(models.Model):
    seller_id = models.CharField(max_length=256,unique=True)
    seller_name = models.CharField(max_length=256)
    seller_number = models.CharField(max_length=256)
    seller_address = models.CharField(max_length=256)


    def __str__(self):
        return self.seller_id


class Customer(models.Model):
    customer_id = models.CharField(max_length=256,unique=True)
    customer_name = models.CharField(max_length=256)
    customer_number = models.CharField(max_length=256)
    customer_address = models.CharField(max_length=256)


    def __str__(self):
        return self.customer_id





class Sales(models.Model):
    seller_id = models.ForeignKey(Seller,related_name='seller_sales',on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,related_name='product_sales',on_delete=models.CASCADE)
    sales_date = models.DateField()
    sales_qty = models.CharField(max_length=256)
    def __str__(self):
        return self.sales_qty


class Purchase(models.Model):
    customer_id = models.ForeignKey(Customer,related_name='customer_sales',on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,related_name='customer_sales',on_delete=models.CASCADE)
    purchase_date = models.DateField()
    purchase_qty = models.CharField(max_length=256)
    def __str__(self):
        return self.purchase_qty
