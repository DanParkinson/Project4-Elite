from django.shortcuts import render, redirect
 # from django.http import HttpResponse # i dont think I need this anymore
from django.contrib.auth import login # allows login 
from django.contrib import messages # allows messages for incomplete signups
from .forms import SignUpForm # connects to forms.py


# Loads the hompage when server runs
def index(request):
    return render(request, "home/index.html") # index load

# handles registration process for POST, GET and ERRORS
def registration(request):
    if request.method == 'POST': # if form is submitted
        form = SignUpForm(request.POST) # uses form in home/forms.py
        if form.is_valid():
            user = form.save() # saves user to the database
            login(request,user) # log in the user after registration
            messages.success(request, 'Registration successful')
            return redirect("index") # Redirects to the homepage if succesful
    else:
        form = SignUpForm() # The user wants to sign up so this loads the form

    return render(request, 'registration/register.html', {"form": form}) # loads the form
