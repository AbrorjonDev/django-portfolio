from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, _('Ro\'yxatdan o\'tish muvaffaqiyatli yakunlandi.'))
            form.save()
            return HttpResponse('muvaffaqiyatli yakunlandi.')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/registration.html', context=context)

# def login(request):
#     if request.method=="POST":
#
#     context = {}
#     return render(request, 'authentication.html', context)
