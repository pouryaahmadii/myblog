from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label="نام",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label="نام خانوادگی",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'})
    )
    email = forms.EmailField(
        label="ایمیل",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
    )
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'})
    )
    password1 = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'})
    )
    password2 = forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar',)

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        label='رمز فعلی',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز فعلی'})
    )
    new_password1 = forms.CharField(
        label='رمز جدید',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز جدید'})
    )
    new_password2 = forms.CharField(
        label='تکرار رمز جدید',
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز جدید'})
    )

    def clean(self):
        cleaned_data = super().clean()
        new1 = cleaned_data.get('new_password1')
        new2 = cleaned_data.get('new_password2')
        if new1 and new2 and new1 != new2:
            raise forms.ValidationError("رمزهای جدید یکسان نیستند.")
        return cleaned_data