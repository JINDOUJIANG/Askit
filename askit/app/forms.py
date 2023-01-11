# app/forms.py

from django import forms

class QuestionForm(forms.Form):
    your_question = forms.CharField(label=False, max_length=50, widget=forms.Textarea(attrs={'placeholder': 'Your question', 'rows': 1, 'cols': 50}))
    body = forms.CharField(label=False, max_length=300, widget=forms.Textarea(attrs={'placeholder': 'Body(optional)', 'rows': 3, 'cols': 50}))
    