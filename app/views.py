from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from app.forms import LoginForm, RegisterForm, UpdateProfileForm, CreateRecipe
from app.models import Recipe
from django.db.models import Q
from app import api
import json 

api_obj = api.Api()

recipe = api.Recipe()
# Create your views here.

# Homepage View
def home_view(request):
    user = request.user

    #NEED TO UPDATE THIS
    featured_recipes = Recipe.objects.all()

    context = {
        'user': user,
        'recipes': featured_recipes
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

# Edit Profile View
def edit_profile_view(request):
    user = request.user

    if request.POST:
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(
            initial= {
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "bio": request.user.bio,
                "location": request.user.location
            }
        )

    context = {
        'user': user,
        'form': form
    }

    template_name = 'edit-profile.html'

    return render(request, template_name, context)

# Create Recipe View
def create_recipe_view(request):
    user = request.user

    if request.POST:
        form = CreateRecipe(request.POST)
        if form.is_valid():
            recipe = form.save()
            if request.POST.get("preference") == "Vegan":
                recipe.is_vegan = True
            elif request.POST.get("preference") == "Gluton-free":
                recipe.is_glutenFree = True
            else:
                recipe.is_vegan = False
            recipe.author = user
            recipe.save()
            return redirect('/')
    else:
        form = UpdateProfileForm()

    context = {
        'user': user,
        'form': form
    }

    template_name = 'create-recipe.html'

    return render(request, template_name, context)

# Recipe View
def recipe_view(request):
    

    #Test data because of api limits
    user = request.user
    data = recipe.read_json("SRPASTA1NNNNN_INFO")
    id = recipe.read_json("SRPASTA1NNNNN")["id"]
    recipe_title = data["title"]
    summary = data["summary"]
    steps = data["instructions"]
    cooking_time = data["cookingMinutes"]
    prep_time = data["preparationMinutes"]
    more_info = data["sourceUrl"]
    ingredents_list = data['extendedIngredients']
    recipe_img = data['image']

    ingredents= []

    recipe.write_json(response= recipe.get_recipe_info_by_id(id = id),key = "SRPASTA1NNNNN_N")

    for i in range(len(ingredents_list)):
       
        ingredents.append(ingredents_list[i]['original'])

    steps_list = steps.split('.')

    steps_list.pop() #gets rid of a '' at the end of the list

    context = {
        'user':user,
        'recipe_title':recipe_title,
        'summary':summary,
        'steps':steps_list ,
        'cooking_time':cooking_time,
        'prep_time':prep_time,
        'more_info':more_info,
        'ingredents':ingredents
        
    }
   
    return render(request,'recipe.html',context)

# Search Results View
def search_results_view(request):
    user = request.user

    if request.method == "POST":
        search_value = request.POST['search_value']

        search_results = Recipe.objects.filter(
        Q(name__icontains=search_value)
        )

    context = {
        'user':user,
        'search_value': search_value,
        'search_results': search_results
    }
    print(search_results)

    return render(request,'search-results.html',context)