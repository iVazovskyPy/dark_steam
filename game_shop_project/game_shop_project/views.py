from django.shortcuts import render
from orders.models import SteamKey
from django.http import JsonResponse


def home(request):
    # Получаем все игры из базы данных
    games = SteamKey.objects.all()

    # Ограничиваем количество игр для отображения (например, 12)
    games_to_display = games[:12]

    # Передаем их в шаблон
    return render(request, 'index.html', {'games': games_to_display})


def load_more_games(request):
    # Получаем параметр start из GET-запроса (индекс начала)
    start = int(request.GET.get('start', 0))

    # Получаем следующие 12 игр
    games = SteamKey.objects.all()[start:start+12]

    # Подготавливаем данные для отправки
    games_data = [
        {
            'title': game.title,
            'price': str(game.price),
            'image_url': game.picture.url if game.picture else '',
        }
        for game in games
    ]

    # Проверяем, есть ли еще игры для загрузки
    has_more = len(games) == 12

    return JsonResponse({'games': games_data, 'has_more': has_more})