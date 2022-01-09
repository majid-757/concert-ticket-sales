from django import forms
from .models import ConcertModel


class SearchForm(forms.Form):
    SearchText = forms.CharField(max_length=100, label="نام کنسرت", required=False)


class ConcertForm(forms.ModelForm):
    class Meta:
        model = ConcertModel
        fields = ['name', 'singername', 'length', 'poster']


