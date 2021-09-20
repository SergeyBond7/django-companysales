from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.db.models import Q
from .models import *
from .forms import *
from django.contrib.auth import login as user_login, logout
from django.contrib import messages

# Customer block --------------------------------------------------------


def customer(request):
    if request.method == 'POST':
        current_id = request.POST.get('id', None)
        customer = get_object_or_404(pk=current_id, klass=Customer)
        customer.delete()
        customer_list = Customer.objects.all()
    else:
        customer_list = Customer.objects.all()
    return render(request, 'customer.html', {'customer_list': customer_list})


def add_customer(request):
    if request.method == 'GET':
        form = AddCustomerForm()
    else:
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'add_object.html', {'form': form})


def edit_customer(request, id):
    if request.method == 'GET':
        customer = get_object_or_404(pk=int(id), klass=Customer)
        form = AddCustomerForm(instance=customer)
    else:
        form = Customer(request.POST)
        body = {**request.POST}
        del body['csrfmiddlewaretoken']
        del body['id']
        for key in body:
            body[key] = body[key][0]
        print(body)
        obj, created = Customer.objects.update_or_create(pk=int(request.POST.get('id')), defaults={**body})
        print(obj, created)
        return redirect('/')
    return render(request, 'edit_customer.html', {'form': form, 'id': id})




# Seller block --------------------------------------------------------

def seller(request):
    if request.method == 'POST':
        current_id = request.POST.get('id', None)
        seller = get_object_or_404(pk=current_id, klass=Seller)
        seller.delete()
        seller_list = Seller.objects.all()
    else:
        seller_list = Seller.objects.all()
    return render(request, 'seller.html', {'seller_list': seller_list})


def add_seller(request):
    if request.method == 'GET':
        form = AddSellerForm()
    else:
        form = AddSellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/seller')
    return render(request, 'add_seller.html', {'form': form})


def edit_seller(request, id):
    if request.method == 'GET':
        seller = get_object_or_404(pk=int(id), klass=Seller)
        form = AddSellerForm(instance=seller)
    else:
        form = Seller(request.POST)
        body = {**request.POST}
        del body['csrfmiddlewaretoken']
        del body['id']
        for key in body:
            body[key] = body[key][0]
        print(body)
        obj, created = Customer.objects.update_or_create(pk=int(request.POST.get('id')), defaults={**body})
        print(obj, created)
        return redirect('/seller')
    return render(request, 'edit_seller.html', {'form': form, 'id': id})


# Product block --------------------------------------------------------

def product(request):
    if request.method == 'POST':
        current_id = request.POST.get('id', None)
        product = get_object_or_404(pk=current_id, klass=Product)
        product.delete()
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.all()
    return render(request, 'product.html', {'product_list': product_list})


def add_product(request):
    if request.method == 'GET':
        form = AddProductForm()
    else:
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product')
    return render(request, 'add_product.html', {'form': form})


def edit_product(request, id):
    if request.method == 'GET':
        product = get_object_or_404(pk=int(id), klass=Product)
        form = ProductUpdateForm(instance=product)
    else:
        form = Product(request.POST)
        body = {**request.POST}
        del body['csrfmiddlewaretoken']
        del body['id']
        for key in body:
            body[key] = body[key][0]
        print(body)
        obj, created = Product.objects.update_or_create(pk=int(request.POST.get('id')), defaults={**body})
        print(obj, created)
        return redirect('/product')
    return render(request, 'edit_product.html', {'form': form, 'id': id})


# Order block --------------------------------------------------------

def order(request):
    order_list = Order.objects.all()
    return render(request, 'order.html', {'order_list': order_list})


def add_order(request):
    if request.method == 'GET':
        form = AddOrderForm()
    else:
        form = AddOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order')
    return render(request, 'add_order.html', {'form': form})


def edit_order(request, id):
    if request.method == 'GET':
        orders = get_object_or_404(pk=int(id), klass=Order)
        form = OrderUpdateForm(instance=orders)
    else:
        body = {**request.POST}
        customer_new = Customer.objects.get(pk=body['customer'][0])
        seller_new = Seller.objects.get(pk=body['seller'][0])
        product_new = Product.objects.get(pk=body['product'][0])
        total_new = body['total'][0]
        date_new = body['date'][0]
        Order.objects.update_or_create(
            pk=int(request.POST.get('id')),
            defaults={
                'customer': customer_new,
                'seller': seller_new,
                'product': product_new,
                'total': total_new,
                'date': date_new
            }
        )
        return redirect('order')
    return render(request, 'edit_order.html', {'form': form, 'id': id})

# Query block --------------------------------------------------------


def no_duplicate(qs_obj):
    result = []
    obj = []
    for i in qs_obj:
        if i.pk not in obj:
            obj.append(i.pk)
            result.append(i)

    return result


def find_1(request):
    form = Find1Form()
    customer_list = Customer.objects.filter(order__seller__pk=request.POST.get('seller'))
    customer_list = no_duplicate(customer_list)

    return render(request, 'find_1.html', {'customer_list': customer_list, 'form': form})


def find_2(request):
    form = Find2Form()
    list_date = Product.objects.filter(order__date=request.POST.get('date'))
    list_date = no_duplicate(list_date)

    return render(request, 'find_2.html', {'form': form, 'list_date': list_date})


def find_3(request):
    form = Find3Form()
    seller_list = Seller.objects.filter(order__product__pk=request.POST.get('product'))
    seller_list = no_duplicate(seller_list)

    return render(request, 'find_3.html', {'form': form, 'seller_list': seller_list})


def find_4(request):
    form = Find3Form()
    customer_list = Customer.objects.filter(order__product__pk=request.POST.get('product'))
    customer_list = no_duplicate(customer_list)

    return render(request, 'find_4.html', {'form': form, 'customer_list': customer_list})


def find_5(request):
    form = Find2Form()
    total_list = Order.objects.filter(date=request.POST.get('date'))
    total_list = no_duplicate(total_list)
    result = []
    for t in total_list:
        result.append(t.total)

    return render(request, 'find_5.html', {'form': form, 'total': sum(result)})


def home(request):
    return render(request, 'customer.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # messages.success(request, 'Вы успешно выполнили вход в систему')
            user = form.get_user()
            user_login(request, user)
            return redirect('/')
        else:
            pass
            # messages.error(request, 'Вы ввели некорректные данные')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('/login')
        else:
            pass
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/auth/login')


def profile_edit(request):
    if request.method == 'GET':
        current_profile = Profile.objects.get(pk=request.user.id)
        if not request.user.is_authenticated:
            return redirect('/auth/login')
        current_profile.first_name = request.user.first_name
        current_profile.last_name = request.user.last_name
        profile_form = ProfileForm(instance=current_profile)
    else:
        current_profile = Profile.objects.get(pk=request.user.id)
        # if profile_form.is_valid():
        current_profile.phone = request.POST.get('phone')
        current_profile.city = request.POST.get('city')
        current_profile.avatar = request.FILES.get('avatar')
        current_profile.save()
        current_profile.user.first_name = request.POST.get('first_name')
        current_profile.user.last_name = request.POST.get('last_name')
        current_profile.user.save()
        profile_form = ProfileForm(request.POST, request.FILES)
        messages.success(request, "You've updated your profile!")
        if profile_form:
            return redirect('/profile_edit')

    return render(request, 'profile_edit.html', {'form': profile_form })







