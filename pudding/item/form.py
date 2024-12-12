from django import forms
from .models import Item

class NewitemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','name','description','price','image',]
        widgets= {
        'category':forms.Select(attrs={'class':'form-control'}),
        'name':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter product name'}),
        'description':forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter product discription'}),
        'price':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter product price'}),
        'image':forms.FileInput(attrs={'class':'form-control'})
        }

class EdititemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','description','price','image',]
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter product name'}),
        'description':forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter product discription'}),
        'price':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter product price'}),
        'image':forms.FileInput(attrs={'class':'form-control'})
        }