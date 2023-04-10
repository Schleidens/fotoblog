from django import forms

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