from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    email = models.EmailField('email', unique=True, blank=False, null=False)
    home_page = models.URLField('home page', max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default=None)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'AppUser'
        verbose_name_plural = 'AppUsers'
