from django.shortcuts import render, get_list_or_404
from django.http import Http404
from .models import FoodType, MenuItem, FoodItemRelationship
from django.views import generic

# Create your views here.


class Menu(generic.ListView):
    context_object_name = 'types'

    def get_queryset(self):
        return FoodType.objects.all()

    # def get_queryset(self):
    #     try:
    #         p = FoodType.objects.all()
    #     except FoodType.DoesNotExist:
    #         raise Http404('please check your database')
    #     return


class Index(Menu):
    template_name = 'index.html'


# def index(request):
#     try:
#         p = FoodType.objects.all()
#     except FoodType.DoesNotExist:
#         raise Http404('Does not exist')
#     return render(request, 'index.html', {'types': p})

class TypeOfFood(Menu):
    template_name = 'menu/menu.html'
    # getting the menu bar

    def get_context_data(self, **kwargs):
        context = super(TypeOfFood, self).get_context_data(**kwargs)
        foodrelationship = get_list_or_404(FoodItemRelationship, type_id=self.kwargs['type_id'])
        context['food'] = MenuItem.objects.filter(items__in=foodrelationship).values().order_by('id')
        context['types'] = FoodType.objects.all()
        return context


class About(Menu):
    template_name = 'about/about.html'

# def foodtype(request, type_id):
#     foodrelationship = get_list_or_404(FoodItemRelationship, type=type_id)
#     item = MenuItem.objects.filter(items__in=foodrelationship).values().order_by('id')
#     return render(request, 'menu/menu.html', {'food': item})

