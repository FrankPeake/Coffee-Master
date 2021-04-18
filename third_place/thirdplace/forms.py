from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class PlaceHolderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        fieldnames = [fieldname for fieldname, _ in self.fields.items()]
        for fieldname in fieldnames:
            field=self.fields.get(fieldname)
            field.widget.attrs.update({'placeholder': field.label})



class SignUpForm(PlaceHolderMixin, UserCreationForm):
    city = forms.CharField(max_length=50, label='City')
    state_province = forms.CharField(max_length=20, label='State/Province')

    class Meta:
            model = User
            fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'city', 'state_province')