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
    # path('move/', views.chat1),
    path('status/', views.status),
    path('chat/', views.chat),
    path('dgdl/', views.dgdl),
      
]
