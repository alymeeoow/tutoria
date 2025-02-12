from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class CustomUserAdmin(UserAdmin):
    model = UserProfile
    list_display = ('username', 'email', 'first_name', 'middle_name', 'last_name', 'role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('middle_name', 'address', 'gender', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('middle_name', 'address', 'gender', 'role')}),
    )

admin.site.register(UserProfile, CustomUserAdmin)
