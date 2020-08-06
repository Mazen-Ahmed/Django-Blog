from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registrationform(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254,required=True)
    password1 = forms.CharField(max_length=30,widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(max_length=30,widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super(registrationform, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2']
