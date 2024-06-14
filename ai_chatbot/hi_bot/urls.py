from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi_bot, name='hi_bot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]