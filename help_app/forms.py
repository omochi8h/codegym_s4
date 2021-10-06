from django import forms


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

