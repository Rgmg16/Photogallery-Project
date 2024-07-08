from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add this line
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/')
    tags = models.CharField(max_length=200)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_photos', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

