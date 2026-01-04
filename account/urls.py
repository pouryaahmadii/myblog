from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.UserDashboardView.as_view() ,name='user_dashboard'),
    path('login/', views.UserLoginView.as_view() ,name='user_login'),
    path('logout/', views.UserLogoutView.as_view() ,name='user_logout'),
    path('register/', views.UserRegisterView.as_view() ,name='user_register'),
    path('profile/<slug:username>', views.UserProfileView.as_view() ,name='user_profile'),
    path('profile/', views.AuthorListView.as_view() ,name='author_profile'),
]
