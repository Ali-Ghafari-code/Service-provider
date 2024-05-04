from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

USER_CHOICES = [
    ('servicer', 'خدمات رسان'),
    ('user', 'کارفرما'),
]


class RegisterForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(  # Changed from forms.CharField to forms.TextInput
            attrs={'class': 'form-control', 'id': 'exampleInputEmail1'},
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'id': 'exampleInputEmail1',
                   'aria-describedby': "emailHelp"}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='کلمه ی عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه ی عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    user_type = forms.ChoiceField(label='نوع کاربر', choices=USER_CHOICES, widget=forms.RadioSelect)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه ی عبور با تکرار آن مطابقت ندارد.')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control', ' id': 'exampleInputEmail1'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='کلمه ی عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )