from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime


TOOL_CHOICES = (
    ('ボール', 'ボール'),
    ('クラブ', 'クラブ'),
    ('リング', 'リング'),
    ('ディアボロ', 'ディアボロ'),
    ('デビルスティック', 'デビルスティック'),
    ('シガーボックス', 'シガーボックス'),
    ('その他', 'その他'),


)

class SignUpForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')


class RecordForm(forms.Form):

    date = forms.DateField(
        label='日時',
        required=True,
        initial=datetime.now(),
        input_formats=[
            '%Y-%m-%d',  # 2010-01-01
            '%Y/%m/%d',  # 2010/01/01
        ]
    )

    name = forms.CharField(
        label='名前',
        max_length=128,
        required=True,
        widget=forms.TextInput(),
        
    )

    tool = forms.ChoiceField(
        label='道具',
        widget=forms.RadioSelect,
        choices=TOOL_CHOICES,
        required=True,
    )

    num = forms.IntegerField(
        label='個数',
        min_value=1,
        max_value=20,
        required=True,
    )

    skill = forms.CharField(
        label='技',
        max_length=30,
        required=True,
        widget=forms.TextInput()
    )

    count = forms.IntegerField(
        label='回数',
        min_value=0,
        max_value=10000,
        required=True,
    )

    publishing = forms.BooleanField(
        label='公開する',
        required=False,
        initial=True,
    )
