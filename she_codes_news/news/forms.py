from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import NewsStory

USER = get_user_model()

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ["title", "pub_date", "content", "image"]
        widgets = {
            "pub_date": forms.DateInput(format=("%d/%m/%Y"),
            attrs={
                "class": "form-control",
                "placeholder": "Select a date",
                "type": "date"
            }),
        }

class SearchForm(forms.Form):
    with_author = forms.ModelChoiceField(
        label='Author',
        queryset=USER.objects.all(),
        required=False
        )
    search = forms.CharField(label="Search", required=False)