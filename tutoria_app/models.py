from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    address = models.TextField(blank=True, null=True)  
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        default='male',
        blank=True, 
        null=True  
    )
    role = models.CharField(
        max_length=10,
        choices=[('parent', 'Parent/Guardian'), ('tutor', 'Tutor')],
        default='parent',
        blank=True, 
        null=True  
    )

    groups = models.ManyToManyField(
        "auth.Group",  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",  
        blank=True
    )

    def __str__(self):
        return self.username
