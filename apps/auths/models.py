from django.contrib.auth.models import AbstractUser
from django.db import models


class UserNet(AbstractUser):
    """Custom user model"""
    
    first_login = models.DateTimeField(auto_now=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=14)
    avatar = models.ImageField(verbose_name='Фото пользователя', upload_to='user/avatar', null=False, blank=True)


    class Meta:
        verbose_name = "Юзер"
        verbose_name_plural = "Юзеры"
