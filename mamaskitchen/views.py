from django.shortcuts import render
from django.http import Http404
from .models import FoodType

# Create your views here.


def index(request):
    # try:
    #
    # except FoodType.DoesNotExist:
    #     raise Http404('Does not exist')

    p = FoodType.objects.all()
    return render(request, 'index.jade', {'types': p})
