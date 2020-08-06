from django.urls import path,include
from . import views
app_name='article'
urlpatterns = [
    path('',views.listarticles,name='all'),
    path('addart/',views.addart,name='addar'),
    path('<int:id>/',views.art,name='viewart'),
    path('<int:id>/delete/',views.deletear,name='del'),
    path('<int:id>/edit/',views.editar,name='edit'),
]
