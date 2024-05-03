from django.urls import path

from new_app import views

urlpatterns = [
 # path('',views.home, name="home"),
 path('dashboard',views.home2, name="home2"),
 path('',views.index, name="index"),
 path('todo',views.todo, name="todo"),
 path('data',views.views_todo,name="views_todo"),
 path("delete/<int:id>/",views.delete,name='delete'),
 path("update/<int:id>/",views.update,name='update')
]