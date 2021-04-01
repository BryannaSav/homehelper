from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", 
                 "email", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        #disables built-in help text on form
        for fieldname in ["first_name", "last_name", "username", 
                         "email", "password1", "password2"]:
            self.fields[fieldname].help_text = None
