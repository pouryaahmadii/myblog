from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView

from blog.models import Article
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PasswordChangeForm
from account.models import Profile
from django.shortcuts import redirect

class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/user_dashboard.html'
    login_url = reverse_lazy('account:user_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_up'] = UserUpdateForm(instance=user)
        context['profile_up'] = ProfileUpdateForm(instance=user.profile)
        context['pass_up'] = PasswordChangeForm(user=user)
        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        user_up = UserUpdateForm(request.POST, instance=user)
        profile_up = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
        if profile_up.is_valid():
            profile_up.save()
        pass_up = PasswordChangeForm(user, request.POST)

        if 'update' in request.POST:
            if user_up.is_valid() and profile_up.is_valid():
                user_up.save()
                profile_up.save()
                messages.success(request, 'پروفایل شما با موفقیت بروز رسانی شد')
                return redirect('account:user_dashboard')
        elif 'change_password' in request.POST:
            if pass_up.is_valid():
                pass_up.save(user)
                update_session_auth_hash(request, user)
                messages.success(request, 'رمز عبور با موفقیت تغییر یافت')
                return redirect('account:user_dashboard')
        elif 'delete' in request.POST:
            user.delete()
            messages.info(request, 'حساب شما حذف شد')

        return self.get(request, *args, **kwargs)


class UserLoginView(LoginView):
    template_name = 'account/user_login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('account:user_dashboard')


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


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home:home')


class UserProfileView(DetailView):
    model = User
    template_name = 'account/user_profile.html'
    context_object_name = 'profile_user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['author_profile'] = Profile.objects.filter(user=self.object).first()
        context['articles'] = Article.objects.filter(author=self.object).order_by('-date',)
        return context
