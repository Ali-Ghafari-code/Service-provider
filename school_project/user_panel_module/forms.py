# forms.py
from django import forms
from account_module.models import User, Servicer
from user_panel_module.models import Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیشنهادات و انتقادات خود را ذکر کنید', 'rows':3}),
        }

    service_id = forms.IntegerField(widget=forms.HiddenInput())





