from django import forms
from .models import New_class
 
 
# creating a form
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = New_class
 
        # specify fields to be used
        fields = [
            "f2",
            "f3",
        ]