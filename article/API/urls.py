from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from .views import *
app_name='final'
urlpatterns = [
  path('',listpa.as_view() ),
  path('<int:pk>/', DetailAPI.as_view()),

]
urlpatterns +=  staticfiles_urlpatterns()
