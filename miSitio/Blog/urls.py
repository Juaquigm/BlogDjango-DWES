from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_editar, name='post_editar'),
    path('post/nuevo/',views.post_nuevo, name='post_nuevo'),
]