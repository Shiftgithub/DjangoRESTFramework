from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('post-todo/', Post_Todo, name="post/todo"),
    path('get-todo/', Get_Todo, name="get/todo"),

]
