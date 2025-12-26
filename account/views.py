from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from account.forms import UserRegisterForm
from account.models import Profile


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/user_dashboard.html'
    login_url = reverse_lazy('account:user_login')

class UserLoginView(LoginView):
    template_name = 'account/user_login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('account:user_dashboard')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home:home')

class UserRegisterView(CreateView):
    model = User
    template_name = 'account/user_register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('account:user_dashboard')

    @transaction.atomic
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        Profile.objects.create(user=user)
        login(self.request, user)
        return response