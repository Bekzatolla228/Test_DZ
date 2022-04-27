from django import forms
from .models import *

class PostCreate(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class AddPostForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Название", widget=forms.TextInput(attrs={"class": "form-input"}))
    content = forms.CharField(widget=forms.Textarea)
    age = forms.IntegerField(label='Age')
    author = forms.CharField(max_length=30, label='Author')
    is_published = forms.BooleanField(label='Public', required=False, initial=True)
    background_color = forms.CharField(max_length=30, label='Color')
    slug = forms.SlugField(max_length=255, label="URL")

    class Meta:
        model = Made_Page
        fields = '__all__'