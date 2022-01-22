from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm, UserForm, ProductForm, SellerForm, CustomerForm, SalesForm, PurchaseForm
from basic_app.models import Product, Seller, Customer ,Sales, Purchase
# Create your views here.

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required







def index(request):
    return render(request, 'basic_app/index.html')

def dashboard(request):
    return render(request, 'basic_app/dashboard.html')

def product_data(request):
    product_list = Product.objects.order_by('product_id')
    product_dict = {'product_data':product_list}
    return render(request, 'basic_app/product_data.html',context=product_dict)

def seller_data(request):
    seller_list = Seller.objects.order_by('seller_id')
    seller_dict = {'seller_data':seller_list}
    return render(request, 'basic_app/seller_data.html',context=seller_dict)

def customer_data(request):
    customer_list = Customer.objects.order_by('customer_id')
    customer_dict = {'customer_data':customer_list}
    return render(request, 'basic_app/customer_data.html',context=customer_dict)

def sales_data(request):
    sales_list = Sales.objects.order_by('-sales_date')
    sales_dict = {'sales_data':sales_list}
    return render(request, 'basic_app/sales_data.html',context=sales_dict)

def purchase_data(request):
    purchase_list = Purchase.objects.order_by('-purchase_date')
    purchase_dict = {'purchase_data':purchase_list}
    return render(request, 'basic_app/purchase_data.html',context=purchase_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registraction.html',
                            {'user_form': user_form,
                              'profile_form':profile_form,
                              'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password {}".format(username,password))
            return render(request, 'basic_app/loginfail.html',{})
    else:
        return render(request, 'basic_app/login.html',{})


def product_form(request):

    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'basic_app/product.html',{'form':form})

def seller_form(request):

    form = SellerForm()

    if request.method == 'POST':
        form = SellerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'basic_app/seller.html',{'form':form})

def customer_form(request):

    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'basic_app/customer.html',{'form':form})

def sales_form(request):

    form = SalesForm()

    if request.method == 'POST':
        form = SalesForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'basic_app/sales.html',{'form':form})

def purchase_form(request):

    form = PurchaseForm()

    if request.method == 'POST':
        form = PurchaseForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'basic_app/purchase.html',{'form':form})
