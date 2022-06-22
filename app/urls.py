from . import views
from django.urls import path
from django.contrib import admin

# Djnago admin header customization
admin.site.site_header = 'Dace admin'
admin.site.site_title = 'Dace admin'
admin.site.index_title = 'Welcome to Dace admin panel!'

  
urlpatterns = [
    path('', views.home, name='home'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('aboutdace/', views.aboutdace, name='aboutdace'),
    path('aboutggv/', views.aboutggv, name='aboutggv'),

 ]