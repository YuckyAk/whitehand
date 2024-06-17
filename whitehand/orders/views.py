from django.shortcuts import render,redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                order = form.save(commit=False)
                order.user = request.user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return redirect('tovari')
    else:
        form = OrderCreateForm
    return render(request, 'cart/order_create.html',
                  {'cart': cart, 'form': form})
