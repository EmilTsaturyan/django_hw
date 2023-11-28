from django.shortcuts import render
from .models import Category, Player

# Create your views here.


def category(request):
    category_list = Category.objects.all()
    return render(request, 'category.html', context={
        'category_list': category_list
    })

def player(request, id):
    category_filter = Category.objects.filter(pk=id)
    return render(request, 'players.html', context={
        'category_filter': category_filter
    })
