from django import forms
from django.forms import ModelForm
from core.models import Product
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from django import forms
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        Widget ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
            'price' :forms.NumberInput(attrs={'class':'form-control'}),
            'product_available_count':forms.NumberInput(attrs={'class':'form-control'}),
            'img':forms.FileInput(attrs={'class':'form-control'}),
        }
        
        
class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '1234 Main St'
        }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Apartment or suite'
    }))
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom=select d-block w=100'
    }))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-controt'
    }))