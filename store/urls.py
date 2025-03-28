from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.register_user, name='register'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_user/', views.update_user, name='update-user'),
    path('update_info/', views.update_info, name='update-user-info'),
    path('product/<int:pk>.', views.product, name='product'),
    path('category/<str:slug>/', views.category, name='category'),
    path('search/', views.search, name='search'),
]
