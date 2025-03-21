from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import CustomUser
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .utils import send_verification_email
from django.contrib import messages

from .mixins import LogoutRequiredMixin, LoginRequiredMixin


# Create your views here.
class Signup(LogoutRequiredMixin, View):
    redirect_to = "signin"

    def get(self, request):
        form = CustomUserCreationForm()
        context = {"form": form}
        return render(request, "signup.html", context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_verified = False
            user.save()

            send_verification_email(user=user, request=request)
            messages.success(request, "plese check your email for verification link.")

            return redirect("signin")

        context = {"form": form}
        return render(request, "signup.html", context)


class Signin(LogoutRequiredMixin, View):

    def get(self, request):
        form = CustomAuthenticationForm()
        context = {"form": form}
        return render(request, "signin.html", context)

    def post(self, request):
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            print("form is valid")

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_verified:
                    login(request, user)
                    print("done")
                    return redirect("home")
                else:
                    print("not verified")
            else:
                print("user not found")
        else:
            print("form is not valid")
            print(form.errors)
            print(form.non_field_errors)

        context = {"form": form}
        return render(request, "signin.html", context)


class Profile(LoginRequiredMixin, View):
    login_url = "signin"

    def get(self, request, username):
        try:
            user = CustomUser.objects.get(username=username)
            return render(request, "profile.html", {"user": user})
        except CustomUser.DoesNotExist:
            return redirect("home")


def email_verification(request, token):
    try:
        user = CustomUser.objects.get(verification_token=token)

        if user.is_verified:
            print("user is already verified")

            return render(request, "email_verification.html")

        user.is_verified = True
        print("user is verified")
        user.save()

        if user.is_authenticated:
            logout(request)

        return render(request, "email_verification.html")
    except CustomUser.DoesNotExist:
        return HttpResponse("No user found")


@login_required(login_url="signin")
def Logout(request):
    logout(request)
    return redirect("signin")
