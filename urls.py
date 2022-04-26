from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.sayHello) ,
    path('', views.index), 
    path('login/', views.login),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('protocol_list/', views.playgame),
    path('reg_dialogue/', views.dialogue),
     path('move/', views.move),
    path('status/', views.status),
    path('chat/', views.chat),
    path('dgdl/', views.dgdl),
    path('assert/', views.move_turn_1),
      
]
