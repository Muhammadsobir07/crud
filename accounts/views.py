from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from .UserBackEnd import UserBackEnd

from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login,logout

from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



def register_page(request):
    return render(request, 'register.html')


def create_profile(request):
    if request.method != "POST":
        return HttpResponse("Xatolik yuz berdi")
    else:
        username = request.POST.get("username")
        ism = request.POST.get("first_name")
        familiya = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        telefon = request.POST.get("telefon")
        try:
            user = Profile.objects.create_user(
                username = username,
                first_name = ism,
                last_name = familiya,
                email = email,
                password = password,
                telefon = telefon,
            )
            user.save()
            return HttpResponseRedirect("/")
        except:
            return HttpResponseRedirect("register_page")

def login_page(request):
    return render(request,'login.html')


def login(request):
    if request.method != "POST":
        return HttpResponse("Xato Sorov")
    else:
        user = UserBackEnd.authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user != None:
            auth_login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.error(request,"Xato Kirish")
            return HttpResponseRedirect("sign_up")

def home(request):
    object_list = Profile.objects.filter(is_superuser = False)
    paginator = Paginator(object_list,1)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    q = request.GET.get('q')
    if q:
        users = object_list.filter(Q(username__contains=q))
    context = {
        "users":users,
        "page":page,
        "paginator":paginator
    }
    return render(request, 'index.html', context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def delete(request,id):
    brbalo = get_object_or_404(Profile, id=id)
    brbalo.delete()
    return redirect("home")