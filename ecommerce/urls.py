from . import views
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import RegisterView, LoginView, guest_register_view
from django.views.generic import TemplateView
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from billing.views import payment_method_view, payment_method_createview
from carts.views import cart_detail_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name="home"),
    path('about/', views.about_page, name="about"),
    path('contact/', views.contact_page, name="contact"),
    path('login/', LoginView.as_view(), name="login"),
    path('checkout/address/create/', checkout_address_create_view, name="checkout_address_create"),
    path('checkout/address/reuse/', checkout_address_reuse_view, name="checkout_address_reuse"),
    path('register/login/', guest_register_view, name="guest_register"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('api/cart/', cart_detail_api_view, name="api-cart"),
    path('cart/', include('carts.urls', namespace='cart')),
    path('billing/payment-method/', payment_method_view, name="billing-payment-method"),
    path('billing/payment-method/create/', payment_method_createview, name="billing-payment-method-endpoint"),
    path('register/', RegisterView.as_view(), name="register"),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
