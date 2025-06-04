from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'birth_date']  # Выберите нужные поля

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Можете изменить форму, например, добавить кастомные поля или стили