from django import forms
from .models import Contact

class UserForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'photo')