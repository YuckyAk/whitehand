from django.urls import re_path

from orders.views import order_create

urlpatterns = [
    re_path(r'^create/$', order_create, name='order_create'),
]