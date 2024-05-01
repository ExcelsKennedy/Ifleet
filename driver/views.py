from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, inspectionForm
from .models import Inspection, OrderAssignment

# Create your views here.
class CustomLoginView(LoginView):
    def get_success_url(self):
        # Redirect to a specific URL upon successful login
        return reverse_lazy('driver-dashboard')
    
@login_required
def driverHome(request):
    inspection = Inspection.objects.all()
    orders = OrderAssignment.objects.all()
    context = {
        'inspection': inspection,
        'orders': orders,
    }
    return render(request, 'drivers/dashboard.html', context)

@login_required
def driverprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) 
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.driverprofile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() 
            messages.success(request, f'Your account has been updated!') 
            return redirect('driver-profile') 
    else:
        u_form = UserUpdateForm(instance=request.user) 
        p_form = ProfileUpdateForm(instance=request.user.driverprofile)

    context = {
        'u_form': u_form, 
        'p_form': p_form
    }
    return render(request, 'drivers/profile.html', context)

@login_required
def inspection(request):
    if request.method == 'POST':
        form = inspectionForm(request.POST)
        if form.is_valid():
            inspection = form.save(commit=False)
            inspection.save()
            messages.success(request, f'Submitted successfully!')
            return redirect('vehicle-inspection')
    else:
        form = inspectionForm()
    return render(request, 'drivers/inspection.html', {'form': form}) 

@login_required
def inspection_history(request):
    inspection = Inspection.objects.all()
    context = {
        'inspection': inspection,
    }
    return render(request ,'drivers/inspection_history.html', context)