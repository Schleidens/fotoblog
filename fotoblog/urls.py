"""fotoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LoginView

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Generic view url,better for redirect the user and don't give it access to the login page once authenticated.
    path('', LoginView.as_view(
            template_name='login.html',
            redirect_authenticated_user=True
    ),  name='login-page'),

    #did the same thing but can't automatically redirect authenticated user. 
    # path('', authentication.views.loginPage.as_view(), name='login-page'),
    
    path('logout', authentication.views.logout_user, name='logout'),
    path('signup', authentication.views.signup_page.as_view(), name='signup-page'),
    path('home/', blog.views.home_page, name='home-page')
]
