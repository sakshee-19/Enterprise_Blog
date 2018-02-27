from django import forms
from blog.models import post
from pagedown.widgets import PagedownWidget


class PostForm(forms.ModelForm):
    post_content = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = post
        fields = ['image','title', 'post_content', ]
