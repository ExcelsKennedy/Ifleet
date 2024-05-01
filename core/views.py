from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import contactForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, f'Submitted successfully!')
            return redirect('contact')
    else:
        form = contactForm()
    return render(request, 'core/contact.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, 'Logged Out') 
        return redirect('login') 
    return render(request, 'core/logout.html') 

def registerHome(request):
    return render(request, 'core/signup_home.html')

def loginHome(request):
    return render(request, 'core/login_home.html')

