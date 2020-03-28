from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'add_todo/',views.add_todo, name="add_todo"),
    path('delete_todo/<int:todo_id>/',views.delete_todo, name="delete_todo"),
]