from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator  # validator for phone number

# django has built in functions for user registration, login and logout. 
# below chooses the wanted fields from User for the sign up form

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(
        max_length=15, 
        required=True,
        validators=[
            RegexValidator(
                regex=r'^\d+$',  # This regex allows only digits
                message='Phone number must be numeric.',
            )
        ]
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

