from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^([0-9]+)/$', views.test, name='question'),
]
