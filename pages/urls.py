from django.http import HttpResponse
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [ 

    path('',views.index, name = 'index'),
    path('about/', views.about,  name = 'about'),
    path('home/', views.home, name =  'home'),

] 
urlpatterns += staticfiles_urlpatterns()