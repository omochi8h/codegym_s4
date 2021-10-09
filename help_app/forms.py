from django import forms
from django.forms import ModelForm
from .models import Houseworks


class ChkForm(forms.Form):
    labels = ['こども', '任せる仕事']

    child = forms.MultipleChoiceField(
        label=labels[0],
        required=False,
        disabled=False,
        widget=forms.RadioSelect(attrs={
            'id': 'child', 'class': 'form-check-input'}))

    task = forms.MultipleChoiceField(
        label=labels[1],
        required=False,
        disabled=False,
        widget=forms.CheckboxSelectMultiple(attrs={
            'id': 'task', 'class': 'form-check-input'}))

# class HouseworksForm(ModelForm):
#     class Meta:
#         model = Houseworks
#         fields = ['job_name']