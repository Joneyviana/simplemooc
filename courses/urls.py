from django.conf.urls import url , patterns
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$' , views.index , name='index'),
    url(r'^/(?P<slug>[\w_-]+)/$', views.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/inscricao/$', views.enrollment, name='enrollment'),
]

