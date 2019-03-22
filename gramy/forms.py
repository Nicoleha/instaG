from .models import Profile,Image,Comments
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user']

