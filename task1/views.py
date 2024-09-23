from django.shortcuts import render
from django.http import HttpResponse
from task1.forms import UserRegister
from task1.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post


# Create your views here.


def platform(request):
    title = 'Магазин "ПарСек"'
    heading = 'Главная страница'
    context = {
        'title': title,
        'heading': heading
    }
    return render(request, 'platform.html', context)


def products(request):
    heading = 'Каталог игр'
    games = Game.objects.all()
    back = 'Вернуться обратно'
    context = {
        'heading': heading,
        'games': games,
        'back': back
    }
    return render(request, 'products.html', context)


def cart(request):
    title = 'Корзина'
    heading = 'Корзина'
    text = 'Извините, Ваша корзина пуста'
    back = 'Вернуться обратно'
    context = {
        'title': title,
        'heading': heading,
        'text': text,
        'back': back
    }
    return render(request, 'cart.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                return HttpResponse("Пароли не совпадают")
            elif int(age) < 18:
                return HttpResponse("Вы должны быть старше 18 лет")
            for user in users:
                if user.name == username:
                    return HttpResponse("Пользователь уже существует")
            Buyer.objects.create(name=username, balance=5000, age=age)
            return HttpResponse(f"Приветствуем {username}!")
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html', {'page_posts': page_posts})


