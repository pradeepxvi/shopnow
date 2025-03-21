from django.shortcuts import redirect


class LogoutRequiredMixin:
    redirect_to = "home"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_to)
        return super().dispatch(request, *args, **kwargs)


class LoginRequiredMixin:
    redirect_to = "signin"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_to)
        return super().dispatch(request, *args, **kwargs)
