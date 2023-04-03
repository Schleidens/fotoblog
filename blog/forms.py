from django import forms

from blog.models import Photo, Blog

class photoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']


class blogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']