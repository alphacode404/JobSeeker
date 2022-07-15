from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Note



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fullname', 'profile_pic', 'age', 'email', 'biography', 'country', 'twitter', 'instagram', 'linkedin', 'facebook', 'employment_status', 'occupation', 'city')
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'biography': forms.Textarea(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram':forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin':forms.TextInput(attrs={'class': 'form-control'}),
            'facebook':forms.TextInput(attrs={'class': 'form-control'}),
            'employment_status': forms.Select(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'})
        }


class NoteForm(forms.ModelForm):
    model = Note
    fields = ('company', 'position', 'date', 'text', 'document')



