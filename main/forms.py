from dataclasses import fields
from django import forms
from .models import Payment,Card,Course
from django.core.exceptions import ValidationError

class CardForm(forms.ModelForm):
    
    class Meta:
        model = Card
        exclude = ('user',)
    def clean(self):
        data=super().clean()
        if not data.get('card_number').isnumeric() or len(data.get('card_number'))!=16:
            raise ValidationError({"card_number": "To'g'ri Son kiriting"})
        return data
class PaymentForm(forms.ModelForm):

    
    class Meta:
        model = Payment
        exclude = ('user',)