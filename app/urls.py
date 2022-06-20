from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('aboutdace/', views.aboutdace, name='aboutdace'),
    path('aboutggv/', views.aboutggv, name='aboutggv'),

 ]