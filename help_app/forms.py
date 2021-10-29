from django import forms
from django.forms import ModelForm
from .models import Houseworks

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings
from django import forms
from help_app.models import *

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

import datetime
from django.utils import timezone

User = get_user_model()

subject = "登録確認"
message_template = """
ご登録ありがとうございます。
以下URLをクリックして登録を完了してください。
"""

def get_activate_url(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return settings.FRONTEND_URL + "/activate/{}/{}/".format(uid, token)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "authcode")

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            self.fields["username"].widget.attrs["class"] = "form-control"
            self.fields["email"].widget.attrs["class"] = "form-control"
            self.fields["password1"].widget.attrs["class"] = "form-control"
            self.fields["password2"].widget.attrs["class"] = "form-control"
            self.fields["authcode"].widget.attrs["class"] = "form-control"
    '''

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.authcode = self.cleaned_data["authcode"]
        user.is_active = False

        if commit:
            user.save()
            activate_url = get_activate_url(user)
            message = message_template + activate_url
            user.email_user(subject, message)
        return user

def activate_user(uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception:
        return False

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True
    return False


class AddChild(forms.Form):
    name = forms.CharField(label='名前')

class AddWork(forms.Form):
    name = forms.CharField(label='名前')
    point = forms.IntegerField(
        label='ポイント',
        max_value=200,
        min_value=0
    )

class ChkForm(forms.Form):
    def get_week():
        today = datetime.date.today()
        year = today.year
        month = today.month
        day = today.day
        last = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
        list = []

        for i in range(7):
            value = str(year) + '-' + str(month) + '-' + str(day)
            option = str(year) + '年' + str(month) + '月' + str(day) + '日'
            tup = (value, option)
            list.append(tup)
            day = int(day) + 1
            if day == '1' or day == '2' or day == '3' or day == '4' or day == '5' or day == '6' or day == '7' or day == '8' or day == '9':
                day = '0' + str(day)

            if month == '12' and int(day) > (last.day):
                year = int(year) + 1
                month = '01'
                day = '01'
            elif int(day) > int(last.day):
                month = int(month) + 1
                day = '01'
        return list
    labels = ['こども', '任せる仕事','コメント']
    date_list = get_week()
    date = forms.ChoiceField(
        label='依頼日',
        required=True,
        choices=date_list
    )

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

    text = forms.CharField(
        label='コメント',
        required=False,
        widget=forms.Textarea
    )





