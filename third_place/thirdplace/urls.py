from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('signin/', views.login, name='login'),
    path('browser/', views.browser, name= 'browser'),
    path('bevbuilder/', views.bevbuilder, name= 'bevbuilder'),
    path('signup/', views.signup, name='signup'),

]