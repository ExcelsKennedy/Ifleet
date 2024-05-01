from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import SignupForm, OrderForm, UserUpdateForm, ProfileUpdateForm 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
def customerSignup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Your account has been created! You are now able to Log in') 
        return redirect('login') 
    else:
        form = SignupForm()
    return render(request, 'customers/register.html', {'form': form}) 

class CustomLoginView(LoginView):
    def get_success_url(self):
        # Redirect to a specific URL upon successful login
        return reverse_lazy('customer-home')

def customerHome(request):
    return render(request, 'customers/customer_home.html')

@login_required
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Assign the current user to the order
            order.save()
            messages.success(request, f'Order submitted successfully!')
            return redirect('order')
    else:
        form = OrderForm()
    return render(request, 'customers/order.html', {'form': form})

@login_required
def customerprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) 
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.customerprofile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() 
            messages.success(request, f'Your account has been updated!') 
            return redirect('customer-profile') 
    else:
        u_form = UserUpdateForm(instance=request.user) 
        p_form = ProfileUpdateForm(instance=request.user.customerprofile)

    context = {
        'u_form': u_form, 
        'p_form': p_form
    }
    return render(request, 'customers/profile.html', context) 

def ifleetCopy(request):
    return render(request, 'customers/ifleet.html')