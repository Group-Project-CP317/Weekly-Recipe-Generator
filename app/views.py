import email
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from app.forms import LoginForm, RegisterForm

# Create your views here.

# Homepage View
def home_view(request):
    user = request.user

    context = {
        'user': user
    }

    template_name = 'home.html'

    return render(request, template_name, context)

# Register View
def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            
            return redirect('home')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    template_name = 'register.html'

    return render(request, template_name, context)

# Login View
def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    template_name = 'login.html'

    return render(request, template_name, context)

# Logout View
def logout_view(request):
    logout(request)

    return redirect('home')

# Profile View
def profile_view(request):
    user = request.user

    context = {
        'user': user
    }

    template_name = 'profile.html'

    return render(request, template_name, context)

# Create Recipe View
def create_recipe_view(request):
    user = request.user

    context = {
        'user': user
    }

    template_name = 'create-recipe.html'

    return render(request, template_name, context)

def recipe_view(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request,'recipe.html',context)