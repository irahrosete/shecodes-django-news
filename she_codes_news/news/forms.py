from django import forms
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ["title", "author", "pub_date", "content"]
