# from django import forms
#
#
# class Registration(forms.ModelForm):
from django import forms

from account.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8,required=True,widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8,required=True,widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password','password_confirmation','firstname',
                  'last_name','image','choices')

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise forms.ValidationError('password did not match')
        return data

    def save(self,commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        return user

