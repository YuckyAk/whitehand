from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView

from .forms import UserRegisterForm, ProductUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages

from handmade.models import Product,Category,Size


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('Login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class Logout(LogoutView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

@login_required
def my_user_profile(request):
    return render(request, 'users/profile.html')

@login_required
def admin_tovars(request):
    if request.user.is_superuser:
        producti = Product.objects.all()
        data={
            'producti':producti
        }
    return render(request,'users/uprav_tovars.html',data)

@login_required
def update_tovar(request,id):
    if request.user.is_superuser:
        product = Product.objects.get(id=id)
        if request.method == 'POST':
            form = ProductUpdateForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect(admin_tovars)
        else:
            categs = Category.objects.all()
            product = Product.objects.get(id=id)
            form = ProductUpdateForm(instance=product)
            manufacturer = Size.objects.all()
            data={
                'categs': categs,
                'product': product,
                'manufacturer': manufacturer,
                'form':form
            }
            return render(request,'users/update_tovar.html',data)