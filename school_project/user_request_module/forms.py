from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    type_choices = [
        ('نگهداری از سالمند', 'نگهداری از سالمند'),
        ('تمیز کردن خانه', 'تمیز کردن خانه'),
        ('تعمیرات خانه', 'تعمیرات خانه'),
        ('کمک در مجالس', 'کمک در مجالس'),
    ]
    gender_choices = [
        ('خانم', 'خانم'),
        ('آقا', 'آقا'),
    ]

    time_choices = [
        ('1', '1 ساعت'),
        ('2', '2 ساعت'),
        ('3', '3 ساعت'),
        ('4', '4 ساعت'),
        ('5', '5 ساعت'),
    ]

    type = forms.ChoiceField(choices=type_choices, label='نوع خدمات مورد نیاز',
                             widget=forms.Select(attrs={'class': 'form-select py-3'}))
    service_date = forms.DateTimeField(label='تاریخ و زمان انجام خدمات', widget=forms.DateTimeInput(
        attrs={'data-jdp': True, 'class': 'form-control py-3', 'placeholder': 'انتخاب تاریخ و زمان'}))
    gender = forms.ChoiceField(choices=gender_choices, label='جنسیت خدمات دهنده',
                               widget=forms.Select(attrs={'class': 'form-select py-3'}))
    service_time = forms.ChoiceField(choices=time_choices, label='ساعت مورد نیاز خدمات',
                                     widget=forms.Select(attrs={'class': 'form-select py-3'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5',
                                                               'placeholder': 'مثال: نوشتن دارو های فرد سالمند یا خواسته های شما برای تعمیر'}),
                                  label='توضیحات لازم و خواسته‌های شما', )

    class Meta:
        model = Service
        fields = ['type', 'gender', 'description', 'price', 'service_date', 'address', 'service_time']
        labels = {
            'type': 'نوع خدمات',
            'gender': 'جنسیت خدمات دهنده',
            'description': 'توضیحات',
            'price': 'هزینه',
            'service_date': 'تاریخ انجام پروژه',
            'address': 'محل انجام خدمات',
            'service_time': 'ساعت خدمت'
        }
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'service_date': forms.DateTimeInput(
                attrs={'class': 'form-control py-3', 'data-jdp': True, 'placeholder': 'تاریخ و زمان انجام'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'gender': forms.Select(attrs={'class': 'form-select py-3'}),
            'service_time': forms.Select(attrs={'class': 'form-select py-3'})
        }
