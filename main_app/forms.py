from typing import Any
from django import forms
from .models import *
from django.core.exceptions import ValidationError

# Create your forms here.

class ContactForm(forms.Form):
    n=forms.CharField(max_length=50,label="نام")
    e=forms.EmailField(max_length=70,label="ایمیل")
    p=forms.CharField(max_length=15,label="تلفن")
    t=forms.CharField(max_length=50,label="موضوع")
    m=forms.CharField(label="پیام شما", widget=forms.Textarea)

    def clean(self):
        c=super().clean()
        p=c.get("p")
        if(len(p)<10):
            raise ValidationError("حداقل از 10 رقم استفاده کنید!")
