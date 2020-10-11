from django.http import HttpResponse
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [ 

    path('',views.index, name = 'index'),
    path('about/', views.about,  name = 'about'),
    path('bootstrap/', views.bootstrap, name =  'bootstrap'),
    path('index/', views.bootstrap, name =  'index'),

] 
urlpatterns += staticfiles_urlpatterns()