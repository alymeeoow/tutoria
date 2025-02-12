from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    address = models.TextField()
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        default='male'
    )
    role = models.CharField(
        max_length=10,
        choices=[('parent', 'Parent/Guardian'), ('tutor', 'Tutor')],
        default='parent'
    )

 
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_profiles", 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_profiles",  
        blank=True
    )

    def __str__(self):
        return self.username  
