from django.urls import path
from . import views
app_name='system'
urlpatterns = [
    path('register/',views.registeration),
    path('login/',views.LogIn,name='login'),
    path('logout/',views.logOut,name='logout'),
    path('profile/',views.Profile,name='profile1'),
    path('<int:id>/',views.userprofile,name='profile2'),
]
