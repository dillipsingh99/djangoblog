from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomAccount

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30)

    class Meta(UserCreationForm.Meta):
        model = CustomAccount
        fields = ('username', 'email', 'age','img', 'first_name', 'last_name', 'contact_number','address', 'education', )

class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = CustomAccount
        fields = ('username', 'email', 'age','img', 'first_name', 'last_name', 'contact_number', 'address', 'education',)

        