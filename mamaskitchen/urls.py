from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^type/(?P<type_id>[0-9]+)$', views.TypeOfFood.as_view()),
    url(r'^about$', views.About.as_view(), name='about'),
]