from django import forms
from .models import *



class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktops
        fields = ('type', 'price', 'status', 'issues')
        

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = ('type', 'price', 'status', 'issues')
