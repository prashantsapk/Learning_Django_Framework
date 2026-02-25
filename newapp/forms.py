from django import forms
from .models import Newappvarity

class ChaiVarityForm(forms.Form):
    chai_varity= forms.ModelChoiceField(queryset=Newappvarity.objects.all(),label="Select chai variety")