from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('syllabus/', views.syllabus, name='syllabus'),

]