from django.conf.urls import url
from first_app import views
from django.urls import path

urlpatterns = [
    url(r'^$',views.index,name='index'),
    #path('',views.index,name='index')
]