from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # For index page
    path('', views.Index.as_view(), name='index'),
    
    # Get waist size
    path('get_waist/', views.get_waist, name="get_waist"),
    
    # Update waist size
    path('update_waist/', views.update_waist, name="update_waist"),
]
