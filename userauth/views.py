from django.shortcuts import render
from django.views import generic
from mamaskitchen.views import Menu

# Create your views here.


class Login(Menu):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
