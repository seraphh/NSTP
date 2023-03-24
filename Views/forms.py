from django.forms import ModelForm, TextInput, PasswordInput, CharField, Form
from django.contrib.auth.models import User
from Models.models import Books
class UserRegistration(ModelForm):
    confirm_password = CharField(widget = PasswordInput(render_value=True, attrs = {'placeholder' : 'Confirm Password', 'class' : "form-control"}))
    class Meta:
        model = User 
        
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', 'autocomplete' : 'off'}),
            'password': PasswordInput(attrs={'placeholder': 'Password', 'class' : 'form-control'}),
           

        }
        fields = ['username', 'password']   

class LoginForm(Form):
    username = CharField(max_length=32)
    password = CharField(widget = PasswordInput(attrs={'placeholder': 'Password', 'class' : 'form-control'}))
    username.widget.attrs.update({'placeholder': 'Username', 'class': 'form-control', 'autocomplete' : 'off'})


class BooksForm(Form):
    title = CharField(max_length=32, required=False)
    title.widget.attrs.update({'placeholder': 'Title', 'class': 'form-control', 'autocomplete' : 'off'})



  
       