from django.urls import path
from . import views

urlpatterns = [
    path('signIn', views.signIn, name='users-signin'),
    path('signUp', views.signUp, name='users-signup'),
    path('logout', views.logoutUser, name='users-logout'),

]