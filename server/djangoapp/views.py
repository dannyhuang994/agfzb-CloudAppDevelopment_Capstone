from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)



# `about` view to render a static about page
def about(request):
    context = {}
    return render(request, "djangoapp/about.html", context)


#`contact` view to return a static contact page
def contact(request):
    context = {}
    return render(request, "djangoapp/contact.html", context)

#  `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)

# `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')

#`registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == "GET":
        return render(request, "djangoapp/registration.html", context)
    elif request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        password = request.POST.get("psw")
        user_exist = False
        
        try:
            User.objects.get(username = username)
            user_exist = True
        except:
            logger.debug(f"{username} is new user")
    
        if not user_exist:
            user = User.objects.create_user(
                username=username,
                last_name = last_name,
                first_name = first_name,
                password = password
            )
            login(request, user)
            
            return redirect("djangoapp:index", context)
        else:
            return render(request, 'djangoapp/login.html', context)


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    pass
# ...

# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    pass
# ...

