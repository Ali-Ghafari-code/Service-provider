# forms.py
from django import forms
from account_module.models import User, Servicer


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fullname', 'email', 'national_number', 'mobile_number', 'birth_date', 'address', 'city']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'national_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ServicerProfileForm(forms.ModelForm):
    class Meta:
        model = Servicer
        fields = ['gender', 'certificate', 'experience', 'description']
        widgets = {
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'certificate': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea1', 'rows': 3}))





