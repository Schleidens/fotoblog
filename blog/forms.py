from django import forms
from django.contrib.auth import get_user_model

from blog.models import Photo, Blog

class photoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']


class blogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Blog
        fields = ['title', 'content']


class deleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    

#follow form 
class followUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['follow']