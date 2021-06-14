from django.shortcuts import get_object_or_404, redirect, render
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy


def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            User.objects.create_user(username, "", password)
        except IntegrityError:
            return render(request, "signup.html", {"error": "このユーザーは既に登録されています"})
        except ValueError:
            return render(request, "signup.html", {"error": "ユーザー情報を入力してください"})
    return render(request, "signup.html", {})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("list")
        else:
            return render(request, "login.html", {"context": "ユーザーが登録されていないかユーザー情報が間違っています"})
    return render(request, "login.html", {})


@login_required
def listfunc(request):
    username = request.user.get_username()
    object_list = BoardModel.objects.all()
    return render(request, "list.html", {"object_list": object_list, "username": username})


def logoutfunc(request):
    logout(request)
    return redirect("login")


@login_required
def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, "detail.html", {"object": object})


def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good += 1
    object.save()
    return redirect("list")


def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect("list")
    else:
        object.readtext = object.readtext+" "+username
        object.read += 1
        object.save()
        return redirect("list")


class BoardCreate(CreateView):
    template_name = "create.html"
    model = BoardModel
    fields = ("title", "content", "author", "snsimage")
    success_url = reverse_lazy("list")
