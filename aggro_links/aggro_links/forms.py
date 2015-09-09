from django import forms
from django.contrib.auth.models import User

class UsernameForm(forms.Form):
    username = forms.CharField(
        label="Username", 
        max_length="50", 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("Username already exists")
        except User.DoesNotExist:
            return username

    def save(self, email):
        username = self.cleaned_data['username']
        u = User.objects.create_user(
            username=username,
            email=email
            )
        return u
