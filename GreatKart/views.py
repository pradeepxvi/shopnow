from django.shortcuts import HttpResponse, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin, View):
    def get(self, request):
        context = {"loop": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
        return render(request, "home.html", context)
