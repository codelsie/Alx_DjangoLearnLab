from django import forms

class BookSearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100)
