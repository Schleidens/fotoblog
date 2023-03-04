from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from authentication.forms import loginForm
from django.shortcuts import redirect
from django.views.generic import  View

# Create your views here.


#view based on class (CBVs)
class loginPage(View):
    class_form = loginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.class_form()
        message = ''
        return render(
            request,
            self.template_name,
            context={'form': form, 'message': message}
            )

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                username = username,
                password = password
            )

            if user is not None:
                login(request, user)
                return redirect('home-page')
        
        message = "Username or Password isn't valid"
        return render(
            request,
            self.template_name,
            context={
            'form': form,
            'message': message
            }
            )



#view based on function (FBCs)

#this function did the same as the one bellow  but commented while learning CBVs
''''
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
'''

def logout_user(request):
    logout(request)
    return redirect('login-page')
