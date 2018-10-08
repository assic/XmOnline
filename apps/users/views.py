from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
# Create your views here.


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html', {})


def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html", {})
        else:
            pass
    elif request.method == "GET":
        return render(request, "login.html", {})