from django.shortcuts import render, get_list_or_404
from django.http import Http404
from .models import FoodType, MenuItem, FoodItemRelationship
from django.views import generic

# Create your views here.


def index(request):
    try:
        p = FoodType.objects.all()
    except FoodType.DoesNotExist:
        raise Http404('Does not exist')
    return render(request, 'index.html', {'types': p})


def foodtype(request, type_id):
    foodrelationship = get_list_or_404(FoodItemRelationship, type=type_id)
    item = MenuItem.objects.filter(items__in=foodrelationship).values().order_by('id')
    return render(request, 'menu/menu.html', {'food': item})


def about(request):
    return render(request, 'about/about.html', {})
