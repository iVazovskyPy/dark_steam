from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название категории
    description = models.TextField(blank=True, null=True)  # Описание категории

    def __str__(self):
        return self.name


class SteamKey(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Категория
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    key = models.CharField(max_length=50, unique=True)  # Уникальный ключ
    picture = models.ImageField(upload_to='product_images/', blank=True, null=True) # Картинка
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления
    updated_at = models.DateTimeField(auto_now=True)  # Дата обновления

    def __str__(self):
        return self.title