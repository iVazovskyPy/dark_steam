from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'users'


urlpatterns = [
    path('register/', views.register, name='register'),  # URL для регистрации
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Редирект на главную страницу
]