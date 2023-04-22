from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('get_waist/', views.get_waist, name="get_waist"),
    path('update_waist/', views.update_waist, name="update_waist"),
]
