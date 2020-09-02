from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('best9/', views.best9, name='best9'),
    path('cafemap/', views.cafemap, name='cafemap'),
    path('brandmenu/', views.brandmenu, name='brandmenu'),
    path('post/', views.post, name='post'),
    path('post/write/', views.write, name='write'),
    path('view/', views.view, name='view'),
    path('islike/', views.islike, name='islike'),
    path('notlike/', views.notlike, name='notlike'),
    path('update_cnt/', views.update_cnt, name='update_cnt'),
    path('mypage/', views.mypage, name='mypage'),
    path('userpost/', views.userpost, name='userpost'),
    path('remove/', views.remove, name='remove'),
    path('update/', views.update, name='update'),
]