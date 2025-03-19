from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views import View
from .models import CustomUser
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .utils import send_verification_email


# Create your views here.
class Signup(View):

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

            send_verification_email(user=user)

            return redirect("signin")

        context = {"form": form}
        return render(request, "signup.html", context)


class Signin(View):

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


class Profile(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        usernames = ["admin", "wizzee"]
        return self.request.user.username in usernames

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

            return render(request, "verified_page.html")

        user.is_verified = True
        print("user is verified")
        user.save()

        return render(request, "verified_page.html")
    except CustomUser.DoesNotExist:
        return HttpResponse("No user found")


def check_username(user):
    usernames = ["admin", "wizzee"]
    return user.username in usernames


@login_required(login_url="signin")
@user_passes_test(check_username)
def Logout(request):
    logout(request)
    return redirect("signin")
