from django import forms
from . models import Create_Blog

class create_blog_form(forms.ModelForm):
    class Meta:
        model = Create_Blog
        fields = ['title', 'blog_image', 'blog_categery', 'content']