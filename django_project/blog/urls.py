from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'), #empty path means "home page"
]
 