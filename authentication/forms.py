from django import forms



class loginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    password = forms.CharField(max_length=30, widget=forms.PasswordInput,  label='Password')
