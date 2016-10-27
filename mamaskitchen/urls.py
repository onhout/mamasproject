from django.conf.urls import url
from . import views
from .views import Index, About, TypeOfFood

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^type/(?P<type_id>[0-9]+)$', TypeOfFood.as_view()),
    url(r'^about$', About.as_view(), name='about'),
]