from datetime import datetime
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {
        "today": datetime.today()
    }


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin/"


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = "/notes/"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("notes:list")

        return super().get(request, *args, **kwargs)
