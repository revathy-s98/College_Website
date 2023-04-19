from.import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('create_view', views.create_view, name='create_view'),
    path('member/<int:pk>/', views.update_view, name='change'),

    path('member/ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
    path('message',views.message,name='message'),


]