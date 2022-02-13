from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

# HOMEPAGE VIEW
def home_view(request):
    object1 = """Some object queried from the Database, 
                maybe a project or set of project objects"""

    context = {
        # You place objects in here that you want to bring
        # to the front end. You do it just by adding them
        # to this dictionary commonly called context -
        # simply store key and value pairs
        # For example:
        'object1': object1
    }

    template_name = 'home.html'

    return render(request, template_name, context)