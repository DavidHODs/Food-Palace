from django import forms
from customer.models import MenuItem


class MenuForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label='Name'
    )
    
    description = forms.CharField(
        required=True,
        label='Description',
        widget=forms.Textarea(attrs={
            'rows':3,
        })
    )
    
    image = forms.ImageField(
        required=True, 
        label='',
        widget=forms.ClearableFileInput(attrs={
            'multiple':True
        })
        )

    price = forms.DecimalField(
        required=True,
        label='Price'
    )

    
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'image', 'price', 'category']