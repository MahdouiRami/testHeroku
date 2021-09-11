
from django.urls import path
from . import views

urlpatterns = [
    path('', views.nomPage,name='index'),
    path('api', views.ListUsers.as_view(),name='api')
]