from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем пользователя
            messages.success(request, f'Ваш аккаунт создан! Теперь вы можете войти.')
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})