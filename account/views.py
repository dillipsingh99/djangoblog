from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")
from django.contrib.auth.forms import UserCreationForm
from . forms import CustomUserCreationForm
# from django.views.generic.base import TemplateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def profile(request):
    return render(request, 'profile.html')