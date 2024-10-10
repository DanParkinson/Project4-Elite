from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# django has built in functions for user registration, login and logout. 
# below chooses the wanted fields from User for the sign up form

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

