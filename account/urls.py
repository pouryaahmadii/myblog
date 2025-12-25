from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.UserDashboardView.as_view() ,name='user_dashboard'),
    path('login/', views.UserLoginView.as_view() ,name='user_login'),
]