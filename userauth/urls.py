from django.conf.urls import url, include
from . import views

urlpatterns = (
    url(r'^$', views.login, name='login'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)