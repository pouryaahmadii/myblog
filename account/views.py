from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/user_dashboard.html'
    login_url = reverse_lazy('account:user_login')

class UserLoginView(LoginView):
    template_name = 'account/user_login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('account:user_dashboard')