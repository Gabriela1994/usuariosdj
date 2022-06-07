from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.urls import reverse_lazy, reverse
#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
#
from django.views.generic import (
    CreateView,
    View,
)
from django.views.generic.edit import(
    FormView,
)
from .forms import (
    UserRegisterForm, 
    LoginForm,
    ChangePasswordForm,
)
from .models import User


class UserRegisterView(FormView):
    """Registra un usuario"""
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres= form.cleaned_data['nombres'],
            apellidos= form.cleaned_data['apellidos'],
            genero= form.cleaned_data['genero'],
        )
        return super(UserRegisterView, self).form_valid(form)

class Login(FormView):
    """ingresa un usuario en el sistema"""
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(Login, self).form_valid(form)

class Logout(View):
    """salir del sistema"""
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users_app:user_login')
        )

class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('users_app:user_login')
    login_url = reverse_lazy('users_app:user_login')

    def form_valid(self, form):
        user= self.request.user
        userAuth = authenticate(
            username = user.username,
            password = form.cleaned_data['password1'],
        )
        if userAuth:
            new_password = form.cleaned_data['password2']
            user.set_password(new_password)
            user.save()
        else:
            logout(self.request)
        return super(ChangePasswordView, self).form_valid(form)