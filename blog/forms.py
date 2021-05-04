from django.forms import ModelForm
from .models import Comment
from django import forms

# Create the form class.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'post',)