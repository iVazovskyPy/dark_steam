from django.shortcuts import get_object_or_404, redirect
from products.models import SteamKey
from django.shortcuts import render
from .models import Cart, CartItem


def add_to_cart(request, product_id):
    product = get_object_or_404(SteamKey, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)  # Если корзина не существует, создаем новую
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:  # Если товар уже есть в корзине, увеличиваем количество
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')  # Перенаправление на страницу с корзиной


def cart_view(request):
    cart = Cart.objects.get(user=request.user)  # Получаем корзину пользователя
    cart_items = cart.cartitem_set.all()  # Получаем все товары в корзине
    total_price = cart.get_total_price()  # Общая стоимость товаров в корзине
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()  # Удаляем товар из корзины
    return redirect('cart_view')  # Перенаправление на страницу корзины


def clear_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart.cartitem_set.all().delete()  # Удаляем все товары из корзины
    return redirect('cart_view')  # Перенаправление на страницу корзины


