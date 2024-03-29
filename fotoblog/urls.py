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
from django.conf import settings
from django.conf.urls.static import static

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
    path('profile/photo/', authentication.views.changeProfilePhoto.as_view(), name='change-profile-photo'),
    path('home/', blog.views.home_page, name='home-page'),
    path('add/photo/', blog.views.photo_upload.as_view(), name='add-photo'),
    # add photo and blog view CBVs
    path("add/blog", blog.views.blog_and_photo_upload.as_view(), name="add-blog"),
    # url for single blog view
    path('blog/<int:pk>', blog.views.blog_view.as_view(), name='single-blog-view'),
    #url for edit and delete blog
    path('blog/<int:pk>/update',  blog.views.edit_blog_view.as_view(), name='edit-blog'),
    #url for multiple_photo_upload view
    path('add/multiple-photos', blog.views.upload_multiple_photos.as_view(), name='upload-multiple-photos'),
    #url for follow_user_view
    path('follow', blog.views.follow_user_view.as_view(), name='follow')
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)