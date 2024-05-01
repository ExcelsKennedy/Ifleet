from django.urls import path
from .views import CustomLoginView
from django.contrib.auth import views as auth_views
from . import views as user_view
from . import views

urlpatterns = [
    path('customer-login/', CustomLoginView.as_view(template_name='customers/login.html'), name='login'),
    path('register-customer/', user_view.customerSignup, name='signup-customer'),
    path('',views.customerHome, name='customer-home'),
    path('order/', views.order, name='order'),
    path('customerprofile/', user_view.customerprofile, name='customer-profile'),
    path('ifleet-home-customer-copy/', views.ifleetCopy, name='ifleet-customer'),
]
