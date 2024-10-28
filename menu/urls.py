from django.urls import path
from menu import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('foods/<int:id>/', views.food_detail, name='food_detail'),
    path('foods/<int:food_id>/like/', views.toggle_like, name='toggle_like'),
    path('foods/<int:food_id>/comment/', views.add_comment, name='add_comment'),
    path('foods/', views.food_list, name='food_list'),
    path('foods/<int:id>/', views.food_detail, name='food_detail'),
    path('foods/add/', views.food_create, name='food_create'),
    path('foods/update/<int:id>/', views.food_update, name='food_update'),
    path('foods/delete/<int:id>/', views.food_delete, name='food_delete'),
]
