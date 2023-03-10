from django import forms

from blog.models import Photo

class photoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']