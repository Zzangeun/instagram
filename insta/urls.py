from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('<int:post_pk>/like/', views.like, name='like'),
]