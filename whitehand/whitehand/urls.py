"""
URL configuration for whitehand project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as userviews
from handmade.views import *
from users.views import Login, Logout,my_user_profile,admin_tovars,update_tovar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('tovars',tovari, name='tovari'),
    path('tov/<int:id>/',list_tovar,name ='list_tovar'),
    path('tovars/category<int:id>',prodct_cat,name='prodct_cat'),
    path('search/',search,name = 'search'),
    path ('feed/',feedback,name='feedback'),
    path ('contact/',kontakt ,name='kontaktte'),
path ('politicy/',politicy ,name='politicy'),
path ('abous/',abous ,name='abous'),
    path('cart/', include(('cart.urls','cart'), namespace='cart')),
    path('ord/', include(('orders.urls','order'), namespace='orders')),
    path('register/', userviews.register, name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('accounts/profile/', my_user_profile, name='my_profile'),
    path('accounts/admin/tovars/', admin_tovars, name='admin_tov'),
    path('accounts/admin/tovars/<int:id>/', update_tovar, name='one_tovar_adm'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
