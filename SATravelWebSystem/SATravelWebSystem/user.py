from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    username = forms.CharField(
        max_length=10,
        required=True,
        label="姓名"
    )
    sex = forms.CharField(
        max_length=5,
        required=True,
        label="性別"
    )
    phone = forms.CharField(
        max_length=10,
        required=True,
        label="電話"
    )
    password1 = forms.CharField(
        required=True,
        label="密碼",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        required=True,
        label="驗證密碼",
        widget = forms.PasswordInput
    )
    email = forms.EmailField(
        max_length=75,
        required=True,
        label="信箱"
    )
    error_css_class = 'form-error'
    required_css_class = 'form'

    class Meta:
        model = User
        fields = ("username", "sex", "phone", "password1", "password2", "email")
        # widgets = {
        #     'username':TextInput(attrs={'class':'typeData'}),
        #     'password':TextInput(attrs={'class':'typeData'}),
        #     'password2':TextInput(attrs={'class':'typeData'}),
        # }

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.sex = self.cleaned_data["sex"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
