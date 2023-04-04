from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import photoForm, blogForm
from blog.models import Photo

# Create your views here.


@login_required
def home_page(request):
    photo = Photo.objects.all()
    return render(request, 'home.html', context={'photos': photo})

#add login restriction using mixin bcz @decorators can't be applied on CBVs 
#view for upload photo CBVs
class photo_upload(LoginRequiredMixin, View):
    form_class = photoForm
    template = 'photo_upload.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, context={'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)

            photo.uploader = request.user
            photo.save()

            return redirect('home-page')
        
        return render(request, self.template, context={'form': form})


#same view as the photo_upload view bellow but FBVs 
'''
@login_required
def photo_upload(request):
    form = photoForm()

    if request.method == 'POST':
        form = photoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            
            return redirect('home-page')

    return render(request, 'photo_upload.html', context={'form': form})
''' 


class blog_and_photo_upload(LoginRequiredMixin, View):
    photo_form = photoForm
    blog_form = blogForm
    template = 'blog_view.html'
    
    def get(self, request):
        context = {
            'photo_form' : self.photo_form(),
            'blog_form' : self.blog_form()
        }
        return render(request, self.template, context=context)

    def post(self, request):
        photo_form = self.photo_form(request.POST, request.FILES)
        blog_form = self.blog_form(request.POST)
        if all([photo_form.is_valid(), blog_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()

            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.save()

            return redirect('home-page')

        context = {
            'photo_form' : photo_form,
            'blog_form' : blog_form
        }

        return render(request, self.template, context=context)
