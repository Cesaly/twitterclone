from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic.base import View

from authentication.forms import LoginForm, SignUpForm
# Create your views here.


# def loginview(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(request, username=data['username'],
#                                 password=data['password'])
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(
#                     request.GET.get('next', reverse('homepage')))
#     form = LoginForm()
#     return render(request, 'generic_form.html', {'form': form})


class loginview(View):
    html = "generic_form.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.html, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage')))
        return render(request, self.html, {'form': form})


def signupview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage')))
    form = SignUpForm()
    return render(request, 'generic_form.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
