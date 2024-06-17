from django.db.models import Q
from django.shortcuts import render

from handmade.models import *

from handmade.forms import Feedb,CategoryFilterForm

from cart.forms import CartAddProductForm


def index(request):
    categs = Category.objects.all()
    data={
        'categs':categs
    }
    return render(request,'handmade/index.html',data)

def tovari(request):
    producti = Product.objects.all()
    categs = Category.objects.all()
    form = CategoryFilterForm(request.GET or None)
    cart_product_form = CartAddProductForm()
    if form.is_valid():
        categories = form.cleaned_data['categories']
        producti = producti.filter(category__in=categories)

    data = {
        'producti':producti,
        'categs': categs,
        'form': form,
        'cart_product_form':cart_product_form
    }
    return render (request, 'handmade/main.html',data)

def list_tovar (request,id):
    categs = Category.objects.all()
    product = Product.objects.get(id = id)
    manufacturer = Product.objects.all()
    data = {
        'categs': categs,
        'product':product,
        'manufacturer':manufacturer
    }
    return render (request, 'handmade/list.html',data)

def prodct_cat(request,id):
    categs = Category.objects.all()
    producti = Product.objects.filter(category__id = id)
    data = {
        'producti':producti,
        'categs': categs,
    }
    return render(request, 'handmade/main.html', data)


def search(request):
    query = request.GET.get('query', None)
    if query == '':
        query = 'none'
    query = request.GET.get('q')
    product = Product.objects.filter(
        Q(name__icontains=query)
    ).all()
    data={
        'product': product,
        'query':query
    }
    return render(request,'handmade/main.html',data)

def feedback(request):
    if request.method == 'POST':
        fedd = Feedb(request.POST)
        if fedd.is_valid():
            fedd.save()
    else:
        fedd = Feedb()

    data={
        'fedd':fedd
    }
    return render(request, 'handmade/index.html',data)


def abous(request):
    categs = Category.objects.all()
    data = {
        'categs': categs
    }
    return render(request, 'handmade/onas.html',data)

def politicy(request):
    categs = Category.objects.all()
    data = {
        'categs': categs
    }
    return render(request, 'handmade/politic.html',data)

def kontakt(request):
    categs = Category.objects.all()
    data = {
        'categs': categs
    }
    return render(request, 'handmade/kontakt.html',data)