from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scrap', views.scrap, name='scrap'),
    path('scrapa', views.scrapa, name='scrapa'),
    path('scrapta', views.scrapta, name='scrapta'),
    path('scrapcls', views.scrapcls, name='scrapcls'),
]