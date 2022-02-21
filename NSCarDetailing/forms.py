from re import I
from tkinter.tix import Form
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, EmailField, PasswordInput
from django.contrib.auth.models import User

class FormRegistro(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contaseña', widget=PasswordInput)
    password2 = CharField(label='Repetir contaseña', widget=PasswordInput)
    last_name = CharField()
    first_name = CharField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']#, 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contaseña', widget=PasswordInput)
    password2 = CharField(label='Repetir contaseña', widget=PasswordInput)
    last_name = CharField()
    first_name = CharField()
    class Meta:
        model=User
        fields = ['email','password1','password2', 'first_name','last_name'] 
        help_texts = {k:"" for k in fields}
        
