from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignupForm(UserCreationForm):
    middle_name = forms.CharField(required=False)
    address = forms.CharField(widget=forms.Textarea)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    role = forms.ChoiceField(choices=[('parent', 'Parent/Guardian'), ('tutor', 'Tutor')])

    class Meta:
        model = UserProfile
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'address', 'gender', 'role', 'password1', 'password2']
