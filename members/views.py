from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('room_list'))
    else:
        return HttpResponseRedirect(reverse('room_list'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('room_list'))


def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password or not confirm_password:
            return HttpResponseRedirect(reverse('room_list'))

        if password != confirm_password:
            return HttpResponseRedirect(reverse('room_list'))

        user = User.objects.create_user(username, email, password)
        login(request, user)
        return HttpResponseRedirect(reverse('room_list'))

    else:
        return HttpResponseRedirect(reverse('room_list'))