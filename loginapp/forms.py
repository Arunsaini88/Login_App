from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=200)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    pincode = forms.CharField(max_length=20)
    USER_TYPE_CHOICES = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'profile_picture', 'address_line1', 'city', 'state', 'pincode', 'user_type')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_picture']
