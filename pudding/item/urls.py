from django.urls import path

from . import views


app_name = "item"

urlpatterns = [
    path('<int:pk>/',views.detail,name='detail'),
    path('additem/',views.new,name='additem'),
    path('<int:pk>/edit/',views.edit,name='edititems'),
    path('<int:pk>/delete/',views.delete,name='deleteitems'),
]