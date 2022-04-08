from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.core.exceptions import ValidationError


class AddList(forms.ModelForm):
    class Meta:
        model = MainList
        fields = {'title', 'published_date'}


class AddProduct(forms.ModelForm):
    class Meta:
        model = ListDetail
        fields = {'product_list','product_count'}


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'username', 'password'}

    # def pass_check(self):
    #     password = self.cleaned_data['password']
    #     if len(password) < 3:
    #         raise ValidationError('Пароль должен быть длинне 3-х символов')
    #     return password


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
