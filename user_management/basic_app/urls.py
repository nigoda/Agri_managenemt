from django.urls import path
from basic_app import views


app_name = 'basic_app'

urlpatterns=[
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('product/', views.product_form, name='add_product'),
    path('seller/', views.seller_form, name='add_seller'),
    path('customer/', views.customer_form, name='add_customer'),
    path('sales/', views.sales_form, name='add_sales'),
    path('purchase/', views.purchase_form, name='add_purchase'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('product_data/', views.product_data, name='product_data'),
    path('seller_data/', views.seller_data, name='seller_data'),
    path('customer_data/', views.customer_data, name='customer_data'),
    path('sales_data/', views.sales_data, name='sales_data'),
    path('purchase_data/', views.purchase_data, name='purchase_data'),

]
