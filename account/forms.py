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
    first_name = forms.CharField(
        label='نام',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'})
        )
    last_name = forms.CharField(
        label= 'نام خانوادگی',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خانوداگی خود را وارد کنید'})
    )
    email = forms.EmailField(
        label= 'ایمیل',
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ایمیل خود را وارد کنید'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(
        label= 'بیو',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'بیو خود را وارد کنید'})
    )
    address = forms.CharField(
        label= 'آدرس',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'آدرس خود را وارد کنید'})
    )
    phone = forms.CharField(
        label= 'تلفن',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'تلفن را وارد کنید'})
    )
    birth = forms.CharField(
        label='تاریخ تولد',
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    class Meta:
        model = Profile
        fields = ('avatar','bio','address','phone','birth')

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

    def __init__(self, user,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user


    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('پسورد فعلی اشتباه میباشد')
        return old_password


    def clean(self):
        cleaned_data = super().clean()
        new1 = cleaned_data.get('new_password1')
        new2 = cleaned_data.get('new_password2')
        if new1 and new2 and new1 != new2:
            raise forms.ValidationError("رمزهای جدید یکسان نیستند.")
        return cleaned_data
    def save(self, user):
        new_password = self.cleaned_data['new_password1']
        user.set_password(new_password)
        user.save()
        return user