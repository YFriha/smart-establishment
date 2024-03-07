from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length='63')
    password = forms.CharField(max_length='63', widget=forms.PasswordInput())


class EmailForm(forms.Form):
    email_body = forms.CharField(widget=forms.Textarea)