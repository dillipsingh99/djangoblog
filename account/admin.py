from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomAccount

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomAccount
    list_display = ['email', 'username', 'age','img', 'contact_number', 'is_staff', ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'age', 'contact_number', 'img', 'first_name','last_name', 'is_staff', 'password1', 'password2')}
         ),
    )

admin.site.register(CustomAccount, CustomUserAdmin)


