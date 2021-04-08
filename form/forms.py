
from django import forms
from form.models import Form

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Form
        fields = '__all__'
