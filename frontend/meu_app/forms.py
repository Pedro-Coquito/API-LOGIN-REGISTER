from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    e_mail = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)