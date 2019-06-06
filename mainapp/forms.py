from django import forms
from .models import *


class AddMessageForm(forms.ModelForm):
    cell = forms.CharField(max_length=100, widget=forms.TextInput(attrs={

        'class': 'form-control-lg',
        'autocomplete': 'off',
    'placeholder': 'Enter cell'}))

    def save(self, commit=True):
        cell_name = self.cleaned_data['cell']
        cell = Cell.objects.get_or_create(name = cell_name)[0]
        self.instance.cell = cell
        return super(AddMessageForm, self).save(commit)

    class Meta:
        model = Message
        fields = ['text']

        widgets = {
        'text' : forms.Textarea(attrs={'rows': 7,'cols':100,'placeholder': 'Enter text'})

                                       }


class LoginCellForm(forms.Form):

    cell = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control-lg',
        'autocomplete': 'off',
    'placeholder': 'Enter cell'}))









