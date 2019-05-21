from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from user.models import Profile
from django.conf import settings
from user.forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):    
    template_name = 'dashboard.html' 
    return render(request, template_name)

def registerUser(request):
    template_name = 'reg.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            #Criando objeto de Profile com os dados preenchidos pelo Form
            profile = Profile()
            profile.username = request.POST['username']
            profile.cellphone =  form.cleaned_data['cellphone']
            profile.birthday = form.cleaned_data['birthday']
            profile.save()
            #Autenticando usuário
            user = authenticate(username = request.POST['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegisterForm()
    context = {
        'form' : form
    }
    return render(request, template_name, context)