from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from account.forms import SignUpForm, TeamForm, LoginForm
from account.models import Team


@require_http_methods(["GET"])
def home(request):
    if request.user.is_authenticated and request.user.account.team:
        return render(request, 'home.html', {"team": request.user.account.team.name})
    else:
        return render(request, 'home.html', {"team": None})


@require_http_methods(["GET", "POST"])
def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('team')
        else:
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'form': form})


@require_http_methods(["GET", "POST"])
def login_account(request):
    form = LoginForm()
    if request.method == "GET":
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
        else:
            return redirect('login')


@login_required
def logout_account(request):
    logout(request)
    return redirect('login')


@login_required
@require_http_methods(["GET", "POST"])
def joinoradd_team(request):
    form = TeamForm()
    if request.method == "GET":
        if request.user.account.team:
            return redirect('home')
        else:
            return render(request, 'team.html', {'form': form})
    else:
        form = TeamForm(request.POST)
        if form.is_valid():
            team_exist = Team.objects.filter(name__exact=form.cleaned_data['name']).first()
            if team_exist:
                team = team_exist
            else:
                jitsi_path = "http://meet.jit.si/" + form.cleaned_data['name']
                team = form.save()
                team.jitsi_url_path = jitsi_path
                team.save()
            request.user.account.team = team
            request.user.account.save()
            return redirect('home')
        else:
            return redirect('team')


@require_http_methods(["GET"])
@login_required
def exit_team(request):
    request.user.account.team = None
    request.user.account.save()
    return redirect('home')
