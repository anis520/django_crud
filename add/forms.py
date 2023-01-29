from django import forms
from .models import Shop_data

class Shop_add(forms.ModelForm):
  class Meta:
    
    label_suffix=' 4 '
    model=Shop_data
    fields=['name','price','slug','brand']