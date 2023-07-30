from django.urls import path
from . import views
urlpatterns = [
    path('data_visualization/', views.data_visualization_view, name='data_visualization'),
    path('workers/', views.Workers_managment_view, name='workers_managment'),
    path('login/', views.Login_infra_view, name='login_infra'),
    path('Upload/', views.Upload_view, name='Upload'),
]