from django.urls import path
from . import views
urlpatterns = [
    path('', views.data_visualization_view, name='data_visualization'),
    path('data_visualization/', views.data_visualization_view, name='data_visualization'),
    path('home/', views.data_visualization_view, name='data_visualization'),
    path('workers/', views.Workers_managment_view, name='workers_managment'),
    path('workers/<int:pk>', views.Workers_managment_edit_view, name='workers_edit'),
    path('login/', views.Login_infra_view, name='login'),
    path('Upload/', views.Upload_view, name='upload'),
    path('logout/', views.logout_user, name='logout'),
    path('delete_users/', views.delete_users, name='delete_users'),
    path('delete/<int:pk>/', views.delete_user, name='delete_user'),
    path('add_employee/', views.add_employee, name='add_employee'),


]