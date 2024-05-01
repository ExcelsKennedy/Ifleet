from django.urls import path
from .views import CustomLoginView
from django.contrib.auth import views as auth_views
from . import views as user_view
from . import views

urlpatterns = [
    path('driver-login/', CustomLoginView.as_view(template_name='drivers/driver_login.html'), name='driver-login'),
    path('',views.driverHome, name='driver-dashboard'),
    path('driverprofile/', user_view.driverprofile, name='driver-profile'),
    path('inspection/', views.inspection, name='vehicle-inspection'),
    path('inspection-history/', views.inspection_history, name='vehicle-inspection-history'),
]