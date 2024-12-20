from django import forms
from django_summernote.widgets import SummernoteWidget

from invitationapp.models import InvitationInfo, InvitationGreetingsInfo, InvitationLocationInfo


class CreateViewForm(forms.ModelForm):
    class Meta:
        model = InvitationInfo
        fields = ['wedding_datetime']


class UpdateViewForm(forms.ModelForm):
    class Meta:
        model = InvitationInfo
        fields = ['wedding_datetime']


class GreetingsViewForm(forms.ModelForm):
    class Meta:
        model = InvitationGreetingsInfo
        fields = ['title', 'greetings']
        widgets = {
            'greetings': SummernoteWidget(),
        }
        labels = {
            'title': '제목',
            'greetings': '인사말'
        }

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control'
        })


class LocationViewForm(forms.ModelForm):
    class Meta:
        model = InvitationLocationInfo
        fields = ['transportation']
        widgets = {
            'transportation': SummernoteWidget(),
        }
