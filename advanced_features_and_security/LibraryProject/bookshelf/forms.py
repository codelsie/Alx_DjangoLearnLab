from django import forms

class ExampleForm(forms.Form):
    q = forms.CharField(required=False, max_length=100)
