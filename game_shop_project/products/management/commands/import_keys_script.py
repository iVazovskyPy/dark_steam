import os
import csv
from django.core.management.base import BaseCommand
from products.models import SteamKey, Category  # Замените your_app на название вашего приложения

class Command(BaseCommand):
    help = "Import Steam keys from CSV file"

    def handle(self, *args, **kwargs):
        # Определяем путь к CSV-файлу (в папке data внутри приложения)
        file_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "steam_keys.csv")
        file_path = os.path.abspath(file_path)  # Преобразуем в абсолютный путь

        # Открываем CSV-файл и загружаем данные
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаем заголовок

            for row in reader:
                title, category_name, price, key = row

                # Находим или создаем категорию
                category_obj, created = Category.objects.get_or_create(name=category_name)

                # Создаём Steam-ключ
                SteamKey.objects.create(
                    title=title,
                    category=category_obj,  # Передаём объект категории
                    price=float(price),
                    key=key
                )

        self.stdout.write(self.style.SUCCESS("✅ Данные успешно загружены в базу!"))