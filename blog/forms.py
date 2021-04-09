from django import forms
from .models import Blog, Image,Comment
from datetime import datetime

class BlogForm(forms.ModelForm):
    created = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)
    class Meta:
        model = Blog
        exclude = ('user','favorites','likes')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)