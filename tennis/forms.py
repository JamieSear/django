from django import forms
from .models import Players

class NewPlayerForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = ['name', 'age', 'wins', 'amount']
        


