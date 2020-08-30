from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('best9/', views.best9, name='best9'),
    path('cafemap/', views.cafemap, name='cafemap'),
    path('brandmenu/', views.brandmenu, name='brandmenu'),
]