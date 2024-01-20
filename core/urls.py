from django.contrib.auth import views as auth_views
from django.urls import path
from .views import base_view, frontpage_view, login_view,signup_view

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
urlpatterns = [
    path('base/', base_view, name='base-view'),
    path('frontpage/', frontpage_view, name='frontpage-view'),
    path('login/', login_view, name='login-view'),
    path('signup/', signup_view, name='signup-view'),
    # Add more URL patterns as needed
]