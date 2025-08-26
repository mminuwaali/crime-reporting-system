from django.views import View
from django.contrib import auth, messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.views.generic import UpdateView

from .forms import SignUpForm, UserProfileForm, CustomPasswordChangeForm


class SignOutView(View):
    def get(self, request):
        auth.logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect("account:sign-in")

    def post(self, request):
        auth.logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect("account:sign-in")


class SignInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("coreapp:dashboard")
        form = AuthenticationForm()
        return render(request, "account/sign-in.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("coreapp:dashboard")
        else:
            return render(request, "account/sign-in.html", {"form": form})


class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("coreapp:dashboard")
        form = SignUpForm()
        return render(request, "account/sign-up.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(request, f"Welcome to Crime Reporting System, {user.username}!")
            return redirect("coreapp:dashboard")
        else:
            return render(request, "account/sign-up.html", {"form": form})


class ProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('account:profile')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, "Your profile has been updated successfully.")
        return super().form_valid(form)


class PasswordChangeView(LoginRequiredMixin, View):
    def get(self, request):
        form = CustomPasswordChangeForm(request.user)
        return render(request, 'account/password_change.html', {'form': form})
    
    def post(self, request):
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account:profile')
        else:
            return render(request, 'account/password_change.html', {'form': form})
