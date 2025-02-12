from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from .models import UserProfile

class CustomUserAdmin(UserAdmin):
    model = UserProfile
    list_display = ('username', 'email', 'first_name', 'middle_name', 'last_name', 'role', 'is_staff', 'is_active')

    fieldsets = (
        ('User Information', {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name', 'address', 'gender', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        ('User Information', {'fields': ('username', 'email', 'password1', 'password2')}),
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name', 'address', 'gender', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    def save_model(self, request, obj, form, change):
        """Ensure password is hashed before saving."""
        if form.cleaned_data.get('password'):
            obj.password = make_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

admin.site.register(UserProfile, CustomUserAdmin)
