from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    
class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'password'}), )
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'repeat password'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        
        if password and password.isdigit():
            self.add_error('password', 'password cannot be fully numeric')

        if repeat_password and password != repeat_password:
            self.add_error('repeat_password', 'passwords does not match')