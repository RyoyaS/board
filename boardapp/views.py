from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth.models import User


def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, "", password)
        except IntegrityError:
            return render(request, "signup.html", {"error": "このユーザーは既に登録されています"})
    return render(request, "signup.html", {"some": 100})
