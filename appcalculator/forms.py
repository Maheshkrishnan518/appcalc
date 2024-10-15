from django import forms  
from .models import Appcalculator,Feature
class FeatureForm(forms.ModelForm):  
    class Meta:  
        model = Feature
        fields = "__all__"  

class AppcalculatorForm(forms.ModelForm):  
    class Meta:  
        model =Appcalculator
        fields = ["category"]

    
    category = forms.ModelChoiceField(
        queryset=Appcalculator.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'})
    )