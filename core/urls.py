
from django.conf.urls import url , patterns
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$' , views.home , name='home'),
    url(r'^contato/' , views.contact , name='contact'),
]
