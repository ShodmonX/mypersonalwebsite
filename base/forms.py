from django.forms import ModelForm, EmailInput, PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm

from . import models

class ArticleForm(ModelForm):
    class Meta:
        model = models.Article
        fields = '__all__'


class UserForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
        exclude = ['groups']

        widgets = {
            'email': EmailInput(attrs={'placeholder': 'Enter your email'}),
            'first_name': TextInput(attrs={'placeholder': 'Enter your name'}),
            'last_name': TextInput(attrs={'placeholder': 'Enter your lastname'}),
            'username': TextInput(attrs={'placeholder': 'Create a username'}),
            }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Create a password'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirm your password'})
        

class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']

