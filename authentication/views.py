from django.shortcuts import render
from django.contrib.auth import authenticate, login
from authentication.forms import loginForm


# Create your views here.

def login_page(request):
    form = loginForm()
    message = ''

    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = 'logged in successfully'
            else:
                message = "Username or Password isn't valid"    
    return render(
        request,
        'login.html',
        context={'form': form, 'message': message}
    )    
