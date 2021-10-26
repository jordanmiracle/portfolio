from django import forms
from .models import Article
from . import views
from django.forms import Form, ChoiceField


CHOICE_LIST = [
    ('', '-----'),
    ('', 'esnath'),
    ('', 'jordanmiracle')
]



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "article_image"]

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
        'author': forms.ChoiceField(choices=CHOICE_LIST)

    }
