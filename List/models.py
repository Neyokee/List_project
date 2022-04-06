from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# from .manager import CustomUserManager

# Create your models here.

class MainList(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название листа')
    published_date = models.DateField(default=timezone.now, verbose_name='Дата создания')
    # product_list = models.ForeignKey('ListDetail', default=None, null=True, on_delete=models.CASCADE)
    log_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class ListDetail(models.Model):
    ID = models.ForeignKey('MainList', null=True, on_delete=models.CASCADE)
    product_list = models.CharField(max_length=200, verbose_name='Продукт')
    product_count = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return self.product_list


# class CreateUser(models.Model):
#     username = models.CharField(max_length=100, verbose_name='Логин')
#     password = models.CharField(max_length=20, verbose_name='Пароль')
