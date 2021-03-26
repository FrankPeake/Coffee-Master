from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.login, name='login'),
    path('browser/', views.browser, name= 'browser'),
    path('bevbuilder/', views.bevbuilder, name= 'bevbuilder'),
    path('signup/', views.signup, name='signup'),

]