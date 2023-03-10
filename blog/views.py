from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import photoForm

# Create your views here.


@login_required
def home_page(request):
    return render(request, 'home.html')

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
            photo.save

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
